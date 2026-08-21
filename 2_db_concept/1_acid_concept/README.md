## Question
![](/assets/q_acid.png)

## Response Section

ACID คือคุณสมบัติ 4 ข้อที่ระบบฐานข้อมูลรับประกันให้กับ transaction

- **A (Atomicity)**: ทำ transaction ทั้งหมด หรือ ไม่ทำเลย
- **C (Consistency)**: ก่อนและหลัง transaction ข้อมูลต้องไม่ละเมิดกฎที่ตั้งไว้ (สม่ำเสมอ)
- **I (Isolation)**: มีการแยกการทำงานของ transaction ถ้าเกิดพร้อมกัน
- **D (Durability)**: มีความทนทานของข้อมูลเมื่อ transaction สำเร็จ

ในความหมายของ ACID ใครรับผิดชอบอะไรบ้าง:

| หลักการ | Database | Application |
|---|---|---|
| Atomicity | operation | กำหนดการทำงานของ transaction |
| Consistency | ควบคุมกฎใน database layer | ควบคุม business logic |
| Isolation | operation | เป็นคนควบคุมและจัดการ level of Isolation |
| Durability | operation | response commit handling |