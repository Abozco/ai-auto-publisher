import requests
import os

HF_TOKEN = os.environ["HF_TOKEN"]
FB_PAGE_ID = os.environ["FB_PAGE_ID"]
FB_TOKEN = os.environ["FB_TOKEN"]
WP_URL = os.environ["WP_URL"]
WP_USER = os.environ["WP_USER"]
WP_PASS = os.environ["WP_PASS"]

# 1. توليد المحتوى
resp = requests.post(
    "https://api-inference.huggingface.co/models/google/flan-t5-large",
    headers={"Authorization": f"Bearer {HF_TOKEN}"},
    json={
        "inputs": "اكتب منشور فيسبوك قصير ومقال 300 كلمة عن الذكاء الاصطناعي"
    }
)

text = resp.json()[0]["generated_text"]

# 2. النشر على فيسبوك
requests.post(
    f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/feed",
    data={
        "message": text,
        "access_token": FB_TOKEN
    }
)

# 3. النشر على ووردبريس
requests.post(
    f"{WP_URL}/wp-json/wp/v2/posts",
    auth=(WP_USER, WP_PASS),
    json={
        "title": "مقال بالذكاء الاصطناعي",
        "content": text,
        "status": "publish"
    }
)
