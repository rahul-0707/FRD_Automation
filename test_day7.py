from playwright.sync_api import Page, expect

# Humare teeno Lego blocks (POM Classes) ko import kar rahe hain
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_e2e_pom_saucedemo(page: Page):
    # 1. Objects banana (Teeno pages ko Playwright ka 'page' de diya)
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    print("\n🌐 Step 1: Login kar raha hoon...")
    login_page.navigate()
    login_page.do_login("standard_user", "secret_sauce")

    print("🎒 Step 2: Item Cart mein daal raha hoon...")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    print("💳 Step 3: Checkout aur Details bhar raha hoon...")
    checkout_page.start_checkout()
    checkout_page.fill_personal_details("QA", "Tester", "123456")
    checkout_page.finish_order()

    # --- THE GRAND FINALE (Assertion) ---
    print("⚖️ Judge check kar raha hai ki Order Success ka message aaya ya nahi...")
    
    # Notice karo: Humne locator bhi checkout_page se hi uthaya hai! Test file ekdum clean hai.
    expect(checkout_page.success_message).to_have_text("Thank you for your order!")
    
    print("🎉 BOOM! POM Architecture wala E2E Test PASS ho gaya!")