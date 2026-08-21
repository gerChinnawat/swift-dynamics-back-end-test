## Question
![](/assets/q_indexing.png)

## Response Section

### ข้อดี
1. ช่วยให้การ scan หาข้อมูลของ row ใน table เร็วขึ้น โดยไม่จำเป็นต้อง scan ทุก row
2. ลด latency ของ query โดยเฉพาะใน table ที่มีจำนวน row ที่เยอะมาก ๆ
3. ลด workload ของ database ในการ query ข้อมูลขนาดใหญ่

### ข้อจำกัด
1. indexing จะไม่ได้ให้ประโยชน์มาก ถ้าจำนวนของข้อมูลน้อย (เหมาะกับฐานข้อมูลขนาดใหญ่)
2. indexing ใช้พื้นที่ใน storage เพื่อจัดเก็บข้อมูลของ index
3. ทำให้การเพิ่ม แก้ไข หรือลบข้อมูลจะช้าลง เพราะต้องไป update index ที่เกี่ยวข้องด้วย