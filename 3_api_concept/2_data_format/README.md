## Question
![](/assets/q_data_format.png)

## Response Section

### ความแตกต่างระหว่าง JSON กับ Protocol Buffer

| หัวข้อ | JSON | Protocol Buffer (Protobuf) |
|---|---|---|
| รูปแบบ | Text-based (มนุษย์อ่านได้) | Binary (มนุษย์อ่านไม่ได้) |
| Schema | ไม่บังคับ (schema-less) | บังคับต้องนิยาม `.proto` schema ก่อน |
| ขนาดข้อมูล | ใหญ่กว่า (มี key, string, whitespace) | เล็กกว่ามาก (binary, ไม่มี field name ติดไปด้วย) |
| ความเร็วในการ serialize/deserialize | ช้ากว่า | เร็วกว่า |
| การรองรับภาษา | รองรับแทบทุกภาษาโดย native (parser ในตัว) | ต้องใช้ compiler (`protoc`) generate code ตาม schema |
| Versioning / backward compatibility | ต้องจัดการเอง | รองรับในตัว (field number, optional fields) |
| Type safety | อ่อน (ไม่มี type checking ตอน parse) | เข้ม (compile-time type checking จาก schema) |
| Debug / ดูข้อมูลตรง ๆ | ง่าย เปิดอ่านได้เลย | ยาก ต้องมี schema ถึงจะแปลงกลับมาอ่านได้ |

### ข้อดี - ข้อเสีย ของแต่ละรูปแบบ

**JSON**
- ข้อดี
  - อ่านและเขียนง่ายด้วยตาเปล่า เหมาะกับการ debug
  - ใช้งานได้ทันทีแทบทุกภาษาโดยไม่ต้อง generate code
  - เหมาะกับ public API / เว็บ ที่ต้องการความยืดหยุ่นและเข้าถึงง่าย
- ข้อเสีย
  - ขนาด payload ใหญ่กว่า ทำให้ bandwidth และ latency สูงกว่า
  - ไม่มี schema บังคับ ทำให้ตรวจสอบความถูกต้องของโครงสร้างข้อมูลยากกว่า
  - serialize/deserialize ช้ากว่า เมื่อข้อมูลปริมาณมาก

**Protocol Buffer**
- ข้อดี
  - ขนาดข้อมูลเล็ก ส่งผ่าน network ได้เร็วและประหยัด bandwidth
  - serialize/deserialize เร็วกว่า JSON มาก เหมาะกับระบบที่ต้อง performance สูง (เช่น microservices, gRPC)
  - มี schema (`.proto`) ทำให้ type-safe และจัดการ versioning/backward compatibility ได้ดี
- ข้อเสีย
  - ไม่ human-readable ต้องมี schema และ tool ถึงจะอ่าน/debug ได้
  - ต้อง generate code จาก `.proto` ก่อนใช้งาน เพิ่มขั้นตอนใน build process
  - ไม่เหมาะกับ public API ทั่วไปที่ต้องการให้ client เข้าถึงง่ายโดยไม่ต้องพึ่ง library เฉพาะ

