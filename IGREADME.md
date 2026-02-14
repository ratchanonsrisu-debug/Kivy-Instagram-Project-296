# Instagram Clone Project
นาย รัชชานนท์  ศรีสุวรรณ์ รหัส 6810110296

### การทำงานของโปรแกรม
แอปพลิเคชัน Instagram Clone พัฒนาด้วยภาษา Python และเฟรมเวิร์ก Kivy
เน้นการใช้งาน ScreenManager เพื่อสลับหน้าจอ และการทำ Dynamic Data ผ่านไฟล์ data.py
หน้า Home ไถฟีด ไลก์ โพสต์ comment
หน้า search เเสดงโพสต์ที่เรากดโพสต์เอง
หน้า Post ให้เราเลือกรูป เขียนคำบรรยายเเล้วกดโพสต์ มันจะไปอยู่ในหน้า search
หน้า Pofile เเสดงชื่อ รูปเรา สถานะ รูป กดเเชร์ลิงค์ขึ้น terminal ได้
โดยรวมคือศึกษาจาก Instagram เเละลองทำ solution ให้คล้ายคลึงกันในเชิงผลลัพธ์


Data Source: ข้อมูลถูกดึงมาจากไฟล์ data.py ซึ่งเก็บข้อมูลโพสต์พื้นฐานไว้ในรูปแบบ List ของ Dictionary

AsyncImage: ในส่วนของแกลเลอรี่และฟีด โปรแกรมใช้ AsyncImage เพื่อโหลดรูปภาพจาก URL แบบ Asynchronous ทำให้ตัวแอปไม่ค้างขณะรอโหลดรูปภาพจากอินเทอร์เน็ต

Random Gallery: ในหน้า Profile และ Post โปรแกรมใช้คำสั่ง range() ร่วมกับ f-string เพื่อสุ่ม ID รูปภาพจาก Unsplash หรือ Picsum ทำให้ทุกครั้งที่เข้าหน้าใหม่ รูปภาพจะถูกสุ่มขึ้นมาไม่ซ้ำกัน

ฟังก์ชันการทำงานของปุ่มหลัก (Key Callbacks)
โปรแกรมมีการเชื่อมโยงระหว่าง Python (Logic) และ KV Language (UI) ผ่านระบบ Callbacks ดังนี้:

ระบบการโพสต์ (Post to Search System):
set_selected_image(url): เมื่อกดที่รูปในแกลเลอรี่ โปรแกรมจะเก็บ URL ของรูปนั้นไว้ในตัวแปร selected_image
process_post(caption): เมื่อกดปุ่ม "Post Now" โปรแกรมจะนำรูปที่เลือกและแคปชั่นจาก TextInput ไปเก็บไว้ใน Global List ใน data.py และสั่งเปลี่ยนหน้าไปยังหน้า Search ทันที

การอัปเดตข้อมูล (Profile & Search Updates):
on_enter(): เป็น Event พิเศษที่จะทำงานทุกครั้งเมื่อผู้ใช้สลับหน้าจอ
ในหน้า Search, ฟังก์ชันนี้จะสั่งล้าง Widget เก่าและดึงข้อมูลโพสต์ล่าสุดจาก USER_POSTS มาวาดใหม่ ทำให้โพสต์ที่เพิ่งสร้างปรากฏขึ้นอย่างถาวร (ตราบที่แอปยังรันอยู่)

ฟังก์ชันเสริม (Interaction):
edit_profile(): ใช้คำสั่งเข้าถึง ids เพื่อเปลี่ยนข้อความชื่อผู้ใช้ในหน้าโปรไฟล์โดยตรง
share_profile(): ใช้คำสั่ง print() เพื่อส่งข้อมูลออกทาง Terminal ซึ่งเป็นวิธีตรวจสอบการทำงานของ Callback ที่เรียบง่ายและเสถียร


ปุ่ม / การทำงาน	รายละเอียดการทำงาน (Callback)
Like Button	เปลี่ยนสีไอคอนหัวใจเมื่อถูกกดในหน้า Home
Comment Button	เมื่อกดจะทำการ Focus ไปที่ช่อง TextInput อัตโนมัติ
Image Selection	เลือกรูปจากแกลเลอรี่ในหน้า Post เพื่อเตรียมอัปโหลด
Post Now	ส่งข้อมูลรูปและแคปชั่นไปแสดงผลถาวรในหน้า Search
Edit Profile	เปลี่ยนชื่อโปรไฟล์โดยการเติมคำว่า (Updated) ต่อท้ายชื่อเดิม
Share Profile	แสดงลิงก์ GitHub ของโปรเจคนี้ใน Terminal (Console)
Navigation: Home	สลับหน้าจอไปยังหน้า Feed หลัก
Navigation: Search	สลับหน้าจอไปยังหน้าค้นหา/รวมโพสต์ที่ผู้ใช้สร้าง
Navigation: Post	สลับหน้าจอไปยังส่วนเลือกรูปภาพเพื่อสร้างโพสต์ใหม่
Navigation: Profile	สลับหน้าจอไปยังหน้าโปรไฟล์ส่วนตัวของผู้ใช้


สถิติของโปรเจค (Project Statistics)
จำนวน Widget: มากกว่า 30 ตัว (รวม AsyncImage, Label, Button, และ Layout ต่างๆ)
จำนวน Commit: 30 Commits (ตามประวัติใน Git Log)
ระยะเวลาพัฒนา: 11 วัน (5 ก.พ. - 15 ก.พ. 2569)

### วิธีรัน
1. `pip install kivy`
2. `python IGmain.py`

ตรวจสอบว่าได้ติดตั้ง Python 3.x และ Kivy Library เรียบร้อยแล้ว (pip install kivy)

ตรวจสอบว่ามีไฟล์ครบทั้ง 3 ไฟล์ในโฟลเดอร์เดียวกัน: IGmain.py, instagram.kv, และ data.py

เปิด Terminal หรือ Command Prompt ในโฟลเดอร์นั้น

พิมพ์คำสั่ง python IGmain.py เพื่อเริ่มการทำงาน