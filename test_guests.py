
import os
from playwright.sync_api import Page, expect

os.environ["automation-workshop-user"] = "ivelinhr@gmail.com"
os.environ["automation-workshop-password"] = "temppa$$"
    

def test_create_guest(page: Page):

    page.goto("https://automation-workshop.hacksoft.io/admin/")

    username_field = page.locator("#id_username")
    username_field.fill(os.environ["automation-workshop-user"])

    password_field = page.locator("#id_password")
    password_field.fill(os.environ["automation-workshop-password"])

    submit_button = page.locator("#login-form > div.submit-row > input[type=submit]")
    submit_button.click()

    expect(page).to_have_url("https://automation-workshop.hacksoft.io/admin/")

    guest_link = page.locator("#reservations-guest > a")
    guest_link.click()

    add_guest_button = page.locator("#nav-sidebar > div > table > tbody > tr.model-guest.current-model > td > a")
    add_guest_button.click()

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