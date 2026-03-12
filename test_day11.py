import pytest
import csv  # Naya Astra: CSV file padhne ke liye!
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage 

# ---------------------------------------------------------
# TO-DO 2: Helper Function (The Reader 👓)
# ---------------------------------------------------------
def get_login_data():
    data_list = []
    
    # File ko 'read' (r) mode mein kholo
    with open("test_data/login_data.csv", mode="r") as file:
        csv_reader = csv.reader(file)
        
        # Pehli line (headings: username,password) ko chhod do (skip)
        next(csv_reader) 
        
        # Ab ek-ek karke baaki lines padho
        for row in csv_reader:
            username = row[0]
            password = row[1]
            # Trick: CSV sab kuch text maanta hai. Humein "True" text ko asli boolean True banana hoga
            is_success = True if row[2] == "True" else False
            
            # List mein ek data set pack karke daal do
            data_list.append((username, password, is_success))
            
    return data_list

# ---------------------------------------------------------
# TO-DO 3: Code ko CSV se jodna 🔗
# Dhyan do: Yahan humne list ki jagah apne function ko bula liya hai ()
# ---------------------------------------------------------
@pytest.mark.parametrize("username, password, is_success", get_login_data())
def test_multiple_logins(page: Page, username, password, is_success):
    
    print(f"\n🕵️‍♂️ Test shuru kar raha hoon for user: {username}")
    
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.do_login(username, password)
    
    if is_success == True:
        print("✅ Check kar raha hoon ki inventory page khula ya nahi...")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        print("❌ Check kar raha hoon ki Error message aaya ya nahi...")
        error_message = page.locator(".error-message-container")
        expect(error_message).to_be_visible()