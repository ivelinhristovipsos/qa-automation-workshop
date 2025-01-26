from .constants import BASE_URL

class GuestListPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}admin/reservations/guest/"

    def add_guest_button(self):
        return self.page.locator("#nav-sidebar > div > table > tbody > tr.model-guest.current-model > td > a")