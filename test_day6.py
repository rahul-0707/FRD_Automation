from playwright.sync_api import Page, expect
# 👇 Yahan humne apni nayi banayi hui POM class ko import kiya hai
from pages.login_page import LoginPage 

def test_login_with_pom(page: Page):
    # 1. Object banana: Playwright ke 'page' ko apni LoginPage class ke hawale karna
    login_page = LoginPage(page)
    
    print("\n🌐 POM ke through website khol raha hoon...")
    # 2. Action: Website par jana
    login_page.navigate()
    
    print("⌨️ POM ke through Login details daal raha hoon...")
    # 3. Action: Login karna (Dekho kitna clean hai, seedha ID aur Password diya)
    login_page.do_login("standard_user", "secret_sauce")
    
    print("⚖️ Judge check kar raha hai...")
    # 4. Assertion: (Rule yaad rakhna - Judge hamesha Test file mein hota hai, Page file mein nahi)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("🎉 POM Test Ekdum Successful!")