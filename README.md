# Git Compare Project

โปรเจ็กต์นี้เป็นแอปพลิเคชันเว็บ (Web App) ที่สร้างด้วย **[Streamlit](https://streamlit.io)** เพื่อ:

- **Clone Git Repository** ตาม URL ที่กำหนด
- **เปรียบเทียบ Branch หรือ Tag** สองตัว แล้วแสดงรายชื่อไฟล์แตกต่าง
- **ดู Diff แบบ Side-by-Side** ของไฟล์ที่มีการเปลี่ยนแปลง
- รองรับ **Custom File Mapping** สำหรับไฟล์ที่ชื่อไม่ตรงกัน
- **ลบโฟลเดอร์เก่า** และ **Clear Cache** อัตโนมัติเมื่อเปลี่ยน URL
- **เก็บ Repository ใน Web Cache** แทนการบันทึกลงเครื่อง
- **สุ่มเลขบัตรประชาชนไทย** พร้อมดูข้อมูลจังหวัดและภาค
- **หน้า Home** สำหรับเลือกใช้งานแต่ละฟีเจอร์และล็อกอินก่อนใช้งาน
- **ล็อกอินด้วย Firebase** โดยใช้ email และรหัสผ่าน

ผู้ใช้ต้องล็อกอินด้วยอีเมลและรหัสผ่านที่หน้า **Home** ก่อนใช้งานฟีเจอร์ต่าง ๆ หากไม่ได้ใช้งานเกิน 30 นาทีระบบจะให้ล็อกอินใหม่
ก่อนใช้งานต้องสร้างไฟล์ `firebase_config.json` จากตัวอย่าง `firebase_config_template.json` เพื่อกำหนดค่าการเชื่อมต่อ Firebase
การติดตั้งควรใช้แพ็กเกจ `pyrebase4` ที่พัฒนาต่อจาก pyrebase พร้อม `pycryptodome`
แทน `pycrypto` เพื่อหลีกเลี่ยงปัญหา SyntaxError ใน Python 3

## วิธีใช้งาน (Local Machine)

1. **Clone โปรเจ็กต์ และติดตั้ง dependencies:**
   git clone https://github.com/Nattakitt-Tin/repo_compare
   cd git_compare_project
   pip install -r requirements.txt

2. **รันแอป Streamlit:**
    streamlit run app.py

## วิธีใช้งานผ่าน Docker

1. **Build Image:**
    docker build -t my-streamlit-app:latest .

2. **CRun Container:**
    docker run -p 8501:8501 my-streamlit-app:latest

เปิดเบราว์เซอร์ที่ http://localhost:8501 เพื่อใช้งานแอป
