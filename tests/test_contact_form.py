from playwright.sync_api import Page, expect

from pages.contact_form_page import Contactpage

def test_with_all_mandatory_fields(page: Page):

    contact_form_page = Contactpage(page)

    print("\nGiven user visits the Contact page")
    contact_form_page.visit_contact_page()

    print ("When they fill the form filed Name with “Reyes Cuesta”")
    contact_form_page.fill_name("Reyes Cuesta")

    print ("And fill the field Email with “test@gmail.com”")
    contact_form_page.fill_email("test@gmail.com")

    print ("And fill the field Message with “Test message”")
    contact_form_page.fill_message("Test message")

    print ("And clicks on Send message")
    contact_form_page.cick_send()

    print ("Then the user must see a success message")
    contact_form_page.success_message()


def test_with_not_valid_email(page: Page):

    contact_form_page = Contactpage(page)
    
    print("\nGiven user visits the Contact page")
    contact_form_page.visit_contact_page()

    print ("When they fill the form filed Name with “Reyes Cuesta”")
    contact_form_page.fill_name("Reyes Cuesta")

    print ("And fill the field Email with “test”")
    contact_form_page.fill_email("test")

    print ("And fill the field Message with “Test message”")
    contact_form_page.fill_message("Test message")

    print ("And clicks on Send message")
    contact_form_page.cick_send()

    print ("Then the user must see an error message")
    contact_form_page.error_message()


def test_send_form_empty_email(page: Page):

    contact_form_page = Contactpage(page)

    print("\nGiven user visits the Contact page")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print("When they fill the form field Name with 'Reyes Cuesta'")
    contact_form_page.fill_name("Reyes Cuesta")
    
    print("And they fill the field Message with 'test message'")
    contact_form_page.fill_message("test message")
    
    print("And clicks on Send message")
    contact_form_page.cick_send()
    
    print("Then the user must see an error message")
    # Buscamos el mensaje que avisa de que el email es obligatorio
    contact_form_page.error_message_no_email()