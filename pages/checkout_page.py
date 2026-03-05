class CheckoutPage:
    def __init__(self, page):
        self.page = page
        
        # 1. Locators (Humari Aankhein)
        self.checkout_btn = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        
        # Yeh locator hum Judge (Assertion) ke liye use karenge
        self.success_message = page.locator(".complete-header")

    # 2. Actions (Humare Haath)
    def start_checkout(self):
        """Cart page par aakar Checkout button dabana"""
        self.checkout_btn.click()

    def fill_personal_details(self, fname, lname, zip_code):
        """Form bharna aur Continue dabana"""
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.postal_code.fill(zip_code)
        self.continue_btn.click()

    def finish_order(self):
        """Aakhri step: Finish button dabana"""
        self.finish_btn.click()