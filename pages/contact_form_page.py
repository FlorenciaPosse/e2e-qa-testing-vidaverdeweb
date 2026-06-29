from playwright.sync_api import Page, expect

class Contactpage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/contact"

    def visit_contact_page (self):
        self.page.goto(self.url)

    def fill_name (self, name):
        self.page.get_by_role("textbox", name="Nombre *").fill(name)

    def fill_email (self, email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def fill_message (self, message):
        self.page.get_by_role("textbox", name="Mensaje *").fill(message)

    def cick_send(self):
        self.page.get_by_role("button", name="Enviar Mensaje").click()

    def success_message (self):
        locator = self.page.get_by_text("¡Mensaje enviado con éxito!Gracias por contactarnos. Te responderemos lo antes posible.")
        expect(locator).to_be_visible()

    def error_message (self):
        locator = self.page.get_by_text("El formato del email no es válido")
        expect(locator).to_be_visible()

    def error_message_no_email (self):
        locator = self.page.get_by_text("el email es obligatorio")
        expect(locator).to_be_visible()