class InventoryPage:
    def __init__(self, page):
        self.page = page
        
        # 1. Locators (Humari Aankhein)
        self.backpack_item = page.locator("text=Sauce Labs Backpack")
        self.add_to_cart_btn = page.locator("//button[@name='add-to-cart']")
        self.cart_icon = page.locator(".shopping_cart_link")

    # 2. Actions (Humare Haath)
    def add_backpack_to_cart(self):
        """Backpack par click karke usko cart mein daalna"""
        self.backpack_item.click()
        self.add_to_cart_btn.click()

    def go_to_cart(self):
        """Upar right corner wale cart icon par click karna"""
        self.cart_icon.click()