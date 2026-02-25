from playwright.sync_api import sync_playwright
import time

def run_robot():
    # Robot ko start karo
    with sync_playwright() as p:
        print("🤖 Robot start ho raha hai...")
        
        # 1. Chrome Browser kholo (headless=False matlab browser hume dikhega)
        # slow_mo=1000 matlab har step ke baad 1 second rukega
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        
        # 2. Naya Tab (Page) kholo
        page = browser.new_page()
        
        # 3. Google website par jao
        print("🌐 Google khol raha hoon...")
        page.goto("https://www.google.com")
        
        # 4. Page ka Title print karo
        print("✅ Page ka Title hai:", page.title())
        
        # 5. Thoda ruko taaki hum dekh sakein
        time.sleep(2)
        
        # 6. Browser band karo
        browser.close()
        print("🏁 Robot ne apna kaam khatam kar diya!")

# Function ko call karo
run_robot()