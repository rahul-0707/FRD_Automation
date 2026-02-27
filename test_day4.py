from playwright.sync_api import Page, expect

def test_login_saucedemo(page: Page):
    print("\n🌐 Sauce Demo khol raha hoon...")
    page.goto("https://www.saucedemo.com/")
    
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    print("🕵️‍♂️ Product dhoond raha hoon...")
    page.locator("text=Sauce Labs Backpack").click()
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")
    
    # ==========================================
    # --- NAYA MISSION: XPATH (The Brahmastra) ---
    # ==========================================
    
    print("🏹 XPath se 'Add to cart' button daba raha hoon...")
    
# Yahan humne lamba naam hata kar asli naam 'add-to-cart' kar diya hai
    print("🏹 XPath se 'Add to cart' button daba raha hoon...")
    page.locator("//button[@name='add-to-cart']").click()
    
    # Remove button ka naam bhi andar sirf 'remove' hota hai
    print("⚖️ Judge check kar raha hai ki button ka naam 'Remove' hua ya nahi...")
    expect(page.locator("//button[@name='remove']")).to_have_text("Remove")
    
    print("🛒 Mission Accomplished! Item successfully cart mein add ho gaya!")