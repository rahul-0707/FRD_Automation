class LoginPage:
    # 1. Setup: Page ko initialize karna
    def __init__(self, page):
        self.page = page
        
        # 2. Locators (Humari Aankhein - Sirf ek jagah define karenge)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    # 3. Actions (Humare Haath - In locators par kya karna hai)
    def navigate(self):
        """Website kholne ka kaam"""
        self.page.goto("https://www.saucedemo.com/")

    def do_login(self, username, password):
        """Username, password daal kar button dabane ka kaam"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()