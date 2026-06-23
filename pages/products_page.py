from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url= "https:// web-qa.dev.adalav.es/products"

    def visit_products_page (self):
        self.page,goto(self.url)

    def verify_titol (self):
        expect(self.page.get_by_role("heading,name:"Cátalogo de Plantas")).to_be_visible()
                                     
     def verify_category (self, category)
     expect (self. )                                
                                          
