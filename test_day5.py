from playwright.sync_api import Page, expect

def test_e2e_checkout_saucedemo(page: Page):
    # 1. Login
    print("\n🌐 Sauce Demo khol raha hoon aur Login kar raha hoon...")
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # 2. Add Item to Cart
    print("🕵️‍♂️ Backpack dhoond kar 'Add to cart' daba raha hoon...")
    page.locator("text=Sauce Labs Backpack").click()
    page.locator("//button[@name='add-to-cart']").click()
    expect(page.locator("//button[@name='remove']")).to_have_text("Remove")
    
    # ==========================================
    # --- YAHAN SE DAY 5 KA NAYA CODE SHURU HOGA ---
    # ==========================================
    # ==========================================
    # --- YAHAN SE DAY 5 KA NAYA CODE SHURU HOGA ---
    # ==========================================
    
    # Step 1: Cart icon par click karna (Class selector)
    print("🛒 Cart khol raha hoon...")
    page.locator(".shopping_cart_link").click()
    
    # Step 2: Checkout button dabana (ID selector)
    print("💳 Checkout button daba raha hoon...")
    page.locator("#checkout").click()
    
    # Step 3: Form bharna (Theth user ki tarah)
    print("📝 Apni details bhar raha hoon...")
    page.locator("#first-name").fill("QA")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("123456")
    
    # Step 4: Continue aur Finish dabana
    print("🚀 Order place kar raha hoon...")
    page.locator("#continue").click()
    page.locator("#finish").click()
    
    # --- THE GRAND FINALE (Assertion) ---
    print("⚖️ Judge check kar raha hai ki Order Success ka message aaya ya nahi...")
    
    # Order complete hone par ek header aata hai jiski class 'complete-header' hoti hai
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
    
    print("🎉 BOOM! End-to-End E-commerce flow successfully test ho gaya!")