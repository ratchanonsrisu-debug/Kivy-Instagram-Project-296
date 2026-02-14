from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.label import Label
from data import get_random_posts
from data import ACCOUNTS, get_random_posts  # ใช้ข้อมูลจาก data.py ที่เราทำไว้
import random
from kivy.uix.image import AsyncImage  # เพิ่มบรรทัดนี้ครับ
from kivy.properties import StringProperty, BooleanProperty  # เพิ่ม BooleanProperty
from data import USER_POSTS, add_new_post
from kivy.uix.button import Button  # เพิ่มบรรทัดนี้เข้าไปครับ


class PostWidget(BoxLayout):
    username = StringProperty("")
    profile_pic = StringProperty("")
    post_image = StringProperty("")
    caption = StringProperty("")
    is_liked = BooleanProperty(False)  # เก็บสถานะไลก์ (เริ่มที่ False)

    def like_post(self):
        print(f"You liked {self.username}'s post!")

    def submit_comment(self, text):
        if text:
            print(f"New comment on {self.username}'s post: {text}")
        else:
            print("Comment cannot be empty!")

    def submit_comment(self, text):
        if text:
            # สร้าง Label ใหม่เพื่อแสดงคอมเมนต์
            new_comment = Label(
                text=f"User_296: {text}", size_hint_y=None, height="30dp", halign="left"
            )
            new_comment.bind(size=new_comment.setter("text_size"))

            # เพิ่ม Label เข้าไปใน list
            self.ids.comments_list.add_widget(new_comment)
            print(f"Comment added: {text}")
        else:
            print("Please enter text")

    def focus_comment(self):
        # ทำให้ช่องพิมพ์ข้อความถูกเลือกพร้อมพิมพ์ทันที
        self.ids.comment_input.focus = True
        print(f"Focusing on comment input for {self.username}")

    def toggle_like(self):
        # สลับสถานะ True/False
        self.is_liked = not self.is_liked
        if self.is_liked:
            print(f"Liked {self.username}'s post!")
        else:
            print(f"Unliked {self.username}'s post!")


class HomeScreen(Screen):
    def on_enter(self):
        # ล้างโพสต์เก่าออกก่อน (ถ้ามี)
        self.ids.feed_container.clear_widgets()

        # ดึงข้อมูลสุ่ม 10 โพสต์
        posts = get_random_posts(10)

        for p in posts:
            # สร้าง Widget โพสต์ และส่งค่าข้อมูลเข้าไป
            post = PostWidget(
                username=p["username"],
                profile_pic=p["profile_pic"],
                post_image=p["post_image"],
                caption=p["caption"],
            )
            self.ids.feed_container.add_widget(post)

    def on_button_click(self):
        print("Button Clicked!")

    pass


class ProfileScreen(Screen):
    profile_pic_url = StringProperty("https://picsum.photos/id/201/100/100")

    def edit_profile(self):
        # Callback 1: เติมคำว่า (Updated) ต่อท้ายชื่อเดิม
        current_name = self.ids.profile_name.text
        if "(Updated)" not in current_name:
            self.ids.profile_name.text = f"{current_name} (Updated)"
            print("Profile Name Updated!")

    def share_profile(self):
        # Callback 2: แสดงลิงก์ใน Terminal
        print("\n" + "=" * 20)
        print("SHARE LINK: https://github.com/User_296/Kivy-Instagram")
        print("=" * 20 + "\n")

    def on_enter(self):
        # 1. สุ่มรูปโปรไฟล์ใหม่ทุกครั้งที่เข้าหน้า (ตามที่คุณต้องการ)
        self.profile_pic_url = (
            f"https://picsum.photos/id/{random.randint(1, 1000)}/100/100"
        )

        # 2. ล้างรูปเก่าในตารางออกก่อน
        self.ids.profile_grid.clear_widgets()

        # 3. สุ่มรูปมาแสดงใน Grid 12 รูป
        for i in range(12):
            img = AsyncImage(
                source=f"https://picsum.photos/id/{random.randint(1, 1000)}/200/200",
                allow_stretch=True,
                keep_ratio=False,
                size_hint_y=None,
                height="120dp",
            )
            self.ids.profile_grid.add_widget(img)

    pass


class PostScreen(Screen):
    selected_image = StringProperty("https://picsum.photos/id/1/600/600")

    def on_enter(self):
        self.ids.gallery_grid.clear_widgets()
        for i in range(9):
            img_url = f"https://picsum.photos/id/{i+20}/200/200"

            # สร้าง Button ที่ไม่มีพื้นหลังปกติ
            btn = Button(
                size_hint_y=None,
                height="120dp",
                background_color=(0, 0, 0, 0),  # ทำให้ปุ่มโปร่งใสเพื่อโชว์รูปข้างหลัง
            )

            # สร้างรูปภาพไว้ข้างหลังปุ่ม
            img = AsyncImage(source=img_url, pos=btn.pos, size=btn.size)

            # ใช้ RelativeLayout เพื่อซ้อนปุ่มไว้บนรูป
            from kivy.uix.relativelayout import RelativeLayout

            layout = RelativeLayout(size_hint_y=None, height="120dp")
            layout.add_widget(img)  # รูปอยู่ล่าง
            layout.add_widget(btn)  # ปุ่มอยู่บน (รับแรงกดได้)

            btn.bind(on_press=lambda x, url=img_url: self.set_selected_image(url))
            self.ids.gallery_grid.add_widget(layout)

    def set_selected_image(self, url):
        self.selected_image = url
        # เปลี่ยนข้อความปุ่ม Post เพื่อบอกว่าเลือกรูปแล้ว (ช่วยเพิ่ม 1 Callback)
        self.ids.post_button.text = "Post selected photo"

    def process_post(self, caption):
        if caption:
            add_new_post(self.selected_image, caption)
            self.manager.current = "search"  # โพสต์เสร็จแล้วไปหน้า Search
            print("Post successful!")

    pass


class SearchScreen(Screen):
    def on_enter(self):
        self.ids.search_container.clear_widgets()
        for p in USER_POSTS:
            # ใช้ PostWidget ตัวเดิมมาแสดงผลในหน้า Search
            post = PostWidget(
                username=p["username"],
                profile_pic=p["profile_pic"],
                post_image=p["post_image"],
                caption=p["caption"],
            )
            self.ids.search_container.add_widget(post)

    pass


class InstagramApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProfileScreen(name="profile"))  # เพิ่มหน้านี้
        sm.add_widget(PostScreen(name="post_page"))  # ตรวจสอบชื่อตรงนี้
        sm.add_widget(SearchScreen(name="search"))  # ตรวจสอบว่ามีบรรทัดนี้

        return sm
        print("App is starting...")
        return sm


if __name__ == "__main__":
    InstagramApp().run()
