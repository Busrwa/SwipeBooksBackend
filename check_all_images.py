# check_all_book_covers.py
import requests
from playwright.sync_api import sync_playwright
import json

# 1️⃣ API'den tüm kitap verilerini çek
API_URL = "https://swipebooksbackend.onrender.com/books/"

response = requests.get(API_URL)
if response.status_code != 200:
    print(f"API hatası: {response.status_code}")
    exit(1)

books = response.json()

# 2️⃣ Playwright ile linkleri kontrol et
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Headless modda çalıştırıyoruz
    page = browser.new_page()

    for book in books:
        url = book.get("cover_image_url", "").strip()

        # Boş URL kontrolü
        if not url:
            print(f"[⚠️] Boş link: ID={book.get('id')} Title='{book.get('title')}'")
            continue

        try:
            # 10 saniye timeout ile URL'yi aç
            page.goto(url, timeout=10000, wait_until="load")
            print(f"[✅] Link açıldı: {url}")
        except Exception as e:
            # Hatalı veya erişilemeyen URL'leri yazdır
            print(f"[⚠️] Link hatası: {url} - {e}")

    browser.close()