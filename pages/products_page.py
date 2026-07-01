from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/products"
        
        #Localizadores de Filtros
        self.search_input = page.get_by_role("searchbox", name="Nombre")
        self.category_select = page.get_by_label("CategoríaTodas las categori")
        self.min_price_input = page.get_by_role("spinbutton", name="Precio mínimo")
        self.max_price_input = page.get_by_role("spinbutton", name="Precio máximo")
        
        #Localizadores de Catálogo
        self.catalog_heading = page.get_by_role("heading", name="Catálogo de Productos")
        self.plants_category = page.get_by_text("Plantas").nth(2)
        self.ficus_heading = page.get_by_role("heading", name="Ficus Lyrata")
        self.ficus_price = page.get_by_text("35.00 €")

    def visit_products_page(self):
        self.page.goto(self.url)


    def filter_by_name(self, name: str):
        self.search_input.fill(name)

    def filter_by_category(self, category_label: str):
        self.category_select.select_option(label=category_label)

    def filter_by_price(self, min_price: str, max_price: str):
        self.min_price_input.fill(min_price)
        self.max_price_input.fill(max_price)

    def verify_product_and_price_visible(self, product_name: str, price: str):
        expect(self.page.get_by_text(product_name)).to_be_visible()
        expect(self.page.get_by_text(price)).to_be_visible()

    def verify_no_products_found_message(self):
        expect(self.page.get_by_text("no se encontraron productos que coincidan")).to_be_visible()


    def verify_page_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    def verify_titol(self):
        expect(self.catalog_heading).to_have_text("Catálogo de Productos")

    def verify_category(self):
        expect(self.plants_category).to_be_visible()

    def verify_product_details(self):
        expect(self.ficus_heading).to_contain_text("Ficus Lyrata")
        expect(self.ficus_price).to_contain_text("35.00 €")       