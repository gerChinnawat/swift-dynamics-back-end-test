## Question
![](/assets/q_idempotency.png)

## Response Section

### ความหมายของ Idempotency

Idempotency คือคุณสมบัติที่ว่า ถ้าเรียก request เดิมซ้ำ ๆ กันหลายครั้ง ผลลัพธ์สุดท้ายของระบบจะเหมือนกับการเรียก 1 ครั้ง แม้ response ที่ได้กลับมาอาจไม่เหมือนกันทุกครั้ง

ในบริบทของ RESTful API แต่ละ HTTP method มีคุณสมบัตินี้ต่างกัน:

| Method | Idempotent | อธิบาย |
|---|---|---|
| GET | ใช่ | อ่านข้อมูล ไม่เปลี่ยน state |
| PUT/PATCH | ใช่ | update/replace ด้วยข้อมูลชุดเดิม ผลลัพธ์สุดท้ายเหมือนเดิมทุกครั้ง |
| DELETE | ใช่ | ลบซ้ำกี่ครั้ง resource ก็หายไปเหมือนเดิม (state สุดท้ายเหมือนกัน) |
| POST | ไม่ | ปกติสร้าง resource ใหม่ทุกครั้งที่เรียก ทำให้ผลลัพธ์ไม่เหมือนเดิม |

### ตัวอย่างการ implement ด้วย Python (อ้างอิง code จริงในโปรเจกต์นี้)

ใช้ตัวอย่างจาก `4_rest_api/apis/views/v1/student.py` ซึ่งเป็น `StudentViewSet` ของโปรเจกต์นี้ ปกติ `POST /v1/students/` (ผ่าน `StudentWriteSerializer` ใน `apis/serializers.py`) ไม่ idempotent เพราะเรียกซ้ำแต่ละครั้งจะสร้าง `Student` (`apis/models.py`) ใหม่ทุกครั้ง

วิธีทำให้ endpoint นี้ idempotent คือ override `create()` ให้เช็ค `Idempotency-Key` header ก่อน ถ้าเคยประมวลผล key นี้ไปแล้วให้คืน response เดิม ไม่สร้างซ้ำ:

```python
# apis/views/v1/student.py
from rest_framework import status, viewsets
from rest_framework.response import Response

from apis.filters import StudentFilter
from apis.models import Student
from apis.serializers import StudentReadSerializer, StudentWriteSerializer

# เก็บ (idempotency_key -> student.id) ของจริงควรเก็บใน cache/DB พร้อม TTL เช่น Redis
idempotency_store = {}


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("classroom").all()
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentReadSerializer
        return StudentWriteSerializer

    def create(self, request, *args, **kwargs):
        idempotency_key = request.headers.get("Idempotency-Key")
        if not idempotency_key:
            return Response(
                {"detail": "Idempotency-Key header is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # เคยเห็น key นี้แล้ว -> คืน student ตัวเดิม ไม่สร้างซ้ำ
        student_id = idempotency_store.get(idempotency_key)
        if student_id is not None:
            student = Student.objects.get(pk=student_id)
            return Response(StudentReadSerializer(student).data, status=status.HTTP_200_OK)

        response = super().create(request, *args, **kwargs)
        idempotency_store[idempotency_key] = response.data["id"]
        return response
```

นอกจากนี้ field `student_code` ใน `Student` model (`apis/models.py:95`) ถูกกำหนด `unique=True` อยู่แล้ว ซึ่งเป็นอีกกลไกหนึ่งที่ช่วยเสริม idempotency ในระดับ database — ถ้า client retry ส่ง `student_code` เดิมซ้ำโดยไม่มี `Idempotency-Key`, database ก็จะ reject การสร้างซ้ำด้วย `IntegrityError` แทนที่จะสร้าง record ซ้อนขึ้นมา
