import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage 

# ---------------------------------------------------------
# TO-DO 1: The Data List (Humara Test Data)
# Format: ("username", "password", "kya_login_pass_hoga?")
# ---------------------------------------------------------
login_data = [
    ("standard_user", "secret_sauce", True),      # Sahi user -> Pass hona chahiye
    ("locked_out_user", "secret_sauce", False),   # Blocked user -> Error aana chahiye
    ("galat_user", "galat_password", False)       # Fake user -> Error aana chahiye
]

# ---------------------------------------------------------
# TO-DO 2: Pytest ka Jadoo (Parameterization)
# Yeh ek tag is single test ko 3 baar chalayega!
# ---------------------------------------------------------
@pytest.mark.parametrize("username, password, is_success", login_data)
def test_multiple_logins(page: Page, username, password, is_success):
    
    print(f"\n🕵️‍♂️ Test shuru kar raha hoon for user: {username}")
    
    # 1. LoginPage ka object banaya (POM magic)
    login_page = LoginPage(page)
    
    # 2. Website kholi aur list se aaya hua username/password daala
    login_page.navigate()
    login_page.do_login(username, password)
    
    # ---------------------------------------------------------
    # TO-DO 3: Smart Judge (Assertion)
    # ---------------------------------------------------------
    if is_success == True:
        print("✅ Check kar raha hoon ki inventory page khula ya nahi...")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        print("❌ Check kar raha hoon ki Error message aaya ya nahi...")
        error_message = page.locator(".error-message-container")
        expect(error_message).to_be_visible()