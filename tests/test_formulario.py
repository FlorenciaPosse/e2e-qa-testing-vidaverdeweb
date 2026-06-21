from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("\nGiven user visits the Contact page")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print ("When they fill the form filed Name with “Reyes Cuesta”")
    page.get_by_role("textbox", name="Nombre *").fill("Reyes Cuesta")

    print ("And fill the field Email with “test@gmail.com”")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print ("And fill the field Message with “Test message”")
    page.get_by_role("textbox", name="Mensaje *").fill("Test message")

    print ("And clicks on Send message")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print ("Then the user must see a success message")
    locator = page.get_by_text("¡Mensaje enviado con éxito!Gracias por contactarnos. Te responderemos lo antes posible.")
    expect(locator).to_have_text("¡Mensaje enviado con éxito!Gracias por contactarnos. Te responderemos lo antes posible.")