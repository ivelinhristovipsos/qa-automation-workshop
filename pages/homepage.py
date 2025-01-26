from .constants import BASE_URL

class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}admin/"

    def goto(self):
        self.page.goto(self.url)

    
    def guest_link_button(self):
        return self.page.locator("#reservations-guest > a")
    

    
