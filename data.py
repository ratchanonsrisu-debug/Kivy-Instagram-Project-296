import random

# รายชื่อ Account และรูปโปรไฟล์
ACCOUNTS = [
    {"user": "Taylor_Official", "pic": "https://picsum.photos/id/101/100/100"},
    {"user": "User_296", "pic": "https://picsum.photos/id/201/100/100"},
    {"user": "Kivy_Coder", "pic": "https://picsum.photos/id/301/100/100"},
    {"user": "Swiftie_Thailand", "pic": "https://picsum.photos/id/401/100/100"},
    {"user": "Python_Master", "pic": "https://picsum.photos/id/501/100/100"},
]

# สุ่มแคปชั่น
CAPTIONS = [
    "Love this vibe! #Swiftie",
    "Working on my Kivy Project! 30 Widgets incoming.",
    "Coding is fun when it works.",
    "Sunday morning coffee.",
    "Learning Python is great!",
]


def get_random_posts(n=10):
    posts = []
    for i in range(n):
        acc = random.choice(ACCOUNTS)
        posts.append(
            {
                "username": acc["user"],
                "profile_pic": acc["pic"],
                "post_image": f"https://picsum.photos/id/{random.randint(1, 1000)}/600/600",
                "caption": random.choice(CAPTIONS),
            }
        )
    return posts


USER_POSTS = []  # ตัวแปรเก็บโพสต์ที่ผู้ใช้สร้างเอง


def add_new_post(image_url, caption):
    new_post = {
        "username": "User_296",
        "profile_pic": "https://picsum.photos/id/201/100/100",
        "post_image": image_url,
        "caption": caption,
    }
    USER_POSTS.append(new_post)
