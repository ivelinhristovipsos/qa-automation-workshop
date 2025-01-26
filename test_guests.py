
import os
import requests
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.guestlistpage import GuestListPage
from pages.pageutils import get_session_cookie
from playwright.sync_api import Page, expect

os.environ["automation-workshop-user"] = "ivelinhr@gmail.com"
os.environ["automation-workshop-password"] = "temppa$$"


def test_create_guest(page: Page):
    login_page = LoginPage(page)
    login_page.goto()

    login_page.login_field().fill(os.environ["automation-workshop-user"])
    login_page.password_field().fill(os.environ["automation-workshop-password"])

    login_page.submit_button().click()

    result = requests.post("https://automation-workshop.hacksoft.io/api/nuke/", cookies=get_session_cookie(page))
    print(result.text)
    
    home_page = HomePage(page)
    expect(page).to_have_url(home_page.url)
    

    home_page.guest_link_button().click()

    guest_list_page = GuestListPage(page)
    expect(page).to_have_url(guest_list_page.url)

    guest_list_page.add_guest_button().click()

    first_name_field = page.locator("#id_first_name")
    first_name_field.fill("Ivelin")

    last_name_field = page.locator("#id_last_name")
    last_name_field.fill("Hristov")

    email_field = page.locator("#id_email")
    email_field.fill("ivelinhr@gmail.com")

    phone_field = page.locator("#id_phone")
    phone_field.fill("1234567890")

    submit_button = page.locator("#guest_form > div > div > input.default")
    submit_button.click()

    success_message = page.locator("#content-start > ul > li")
    expect(success_message).to_be_visible()