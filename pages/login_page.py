import os
from dotenv import load_dotenv

# 1. Tijori kholne ka jadoo! Yeh .env file ko memory mein load kar dega.
load_dotenv()

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        # 2. Hardcoded URL hataya, aur tijori (environment) se BASE_URL nikal liya
        url = os.getenv("BASE_URL")
        self.page.goto(url)

    def do_login(self, username, password):
        self.page.locator("[data-test='username']").fill(username)
        self.page.locator("[data-test='password']").fill(password)
        self.page.locator("[data-test='login-button']").click()