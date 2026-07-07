from playwright.sync_api import Page, expect

class ShoppingCart:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"

    def verify_product_shopping_cart(self,product):
         expect(self.page.get_by_role("heading", name=product)).to_be_visible()

    def verify_product_deleted_from_cart(self,product):
          expect(self.page.get_by_role("heading", name=product)).not_to_be_visible()

    def verify_price_cart(self,price):
        expect(self.page.get_by_text(price).first).to_be_visible()

    def delete_product_cart(self,product):
        self.page.get_by_role("button", name="Eliminar "+product).click()

    def empty_cart(self):
         self.page.get_by_role("button", name="Vaciar Carrito").click()
    
    def verify_empty_cart(self):
         expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()

    def view_products(self):
         self.page.get_by_role("link", name="Ver Productos").click()

    def proceed_to_payment(self):
         self.page.get_by_role("link", name="Proceder al Pago").click()