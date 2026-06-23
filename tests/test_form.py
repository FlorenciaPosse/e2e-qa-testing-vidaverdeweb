from playwright.sync_api import Page, expect

def test_submit_form_with_invalid_email(page: Page):
    print("Given user visit homepage")
    page.goto("https://bootcampqa.com")