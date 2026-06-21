from playwright.sync_api import Page, expect

def test_products_catalog(page: Page):
    print ("\nGiven user visits the Products page")
    page.goto("https://web-qa.dev.adalab.es/products")

    #check that the web's title is “Nuestros Productos | Vida Verde”
    page_title = page.title()
    print ("The web's title is:", page_title)
    expect(page).to_have_title("Nuestros Productos | Vida Verde")
    
    print ("Then the user sees the title “Products catalog”")
    locator = page.get_by_role("heading", name="Catálogo de Productos")
    expect(locator).to_have_text("Catálogo de Productos")

    print ("Then the user sees the category “plants” on the products within that category")
    page.get_by_text("Plantas")
    
    print ("And the user sees a product with the name “Ficus Lyrata”")
    page.get_by_role("heading", name="Ficus Lyrata")

    print ("And the user sees that the product's price is “35.00€”")
    page.get_by_text("35.00 €")