from .constants import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(f"{BASE_URL}admin/")

    def login_field(self):
        return self.page.locator("#id_username")
    
    def password_field(self):
        return self.page.locator("#id_password")
    
    def submit_button(self):
        return self.page.locator("#login-form > div.submit-row > input[type=submit]")