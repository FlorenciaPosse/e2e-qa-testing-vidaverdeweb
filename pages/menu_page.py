from playwright.sync_api import Page, expect

class MenuPage:
    def __init__(self, page: Page):
        self.page = page

    def visitShoppingCart(self):
         self.page.get_by_role("link", name="Carrito de compra").click()

    def finish_purchase(self):
        self.page.get_by_role("link", name="Finalizar Compra").click( )   

    def clic_menu(self, menu_title):
        size = self.page.viewport_size['width']
        if size < 1024:
            self.page.get_by_role("button", name="Abrir menú principal").click()
            self.page.get_by_role("menuitem", name=menu_title).click()
        else:
            self.page.get_by_role("link", name=menu_title).click()