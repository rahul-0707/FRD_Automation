from playwright.sync_api import sync_playwright
import time

def run_robot():
    with sync_playwright() as p:
        print("🤖 Robot start ho raha hai...")
        browser = p.chromium.launch(headless=False, slow_mo=1000) # slow_mo se sab dheere dikhega
        page = browser.new_page()
        
        # 1. Google par jao (Rule 1: Open)
        print("🌐 Google khol raha hoon...")
        page.goto("https://www.google.com")
        
        # --- NAYA MAGIC YAHAN HAI ---
        
        # 2. Search box dhoondo aur type karo (Rule 2: Find & Rule 3: Action)
        print("⌨️ 'FRD Studio' type kar raha hoon...")
        page.locator("[name='q']").fill("FRD Studio")
        
        # 3. Enter dabao (Rule 3: Action)
        print("🎯 Enter daba raha hoon...")
        page.locator("[name='q']").press("Enter")
        
        # ---------------------------
        
        # 4. Result dekhne ke liye thoda wait karo
        time.sleep(3)
        
        # 5. Search hone ke baad page ka naya title print karo
        print("✅ Naya Title hai:", page.title())
        
        browser.close()
        print("🏁 Robot ne apna kaam khatam kar diya!")

run_robot()