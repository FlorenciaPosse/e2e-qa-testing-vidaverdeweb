from playwright.sync_api import Page, expect

def test_product_filters_name_price_category(page: Page):
    print("Given the user visits product page")
    page.goto("https://web-qa.dev.adalab.es/products")


    print("when they filter by name Sanse")
    page.get_by_role("searchbox", name="Nombre").fill("sanse")

    print("and they filter by category Plantas")
    page.get_by_label("CategoríaTodas las categorí").select_option("Plantas")
    
    print("and they filter by minimum price 10")
    page.get_by_role("spinbutton", name="Precio mínimo").fill("10")
    
    print("and they filter by maximum price 25")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")

    print("Then the user must see the product 'sansevieria', category 'plantas' and price '22'")
    expect(page.get_by_text("sansevieria")).to_be_visible()
    expect(page.get_by_text("22")).to_be_visible()


def test_product_filters_name_price_category(page: Page):
    print("Given the user visits product page")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("when they filter by a non-existent name test")
    page.get_by_role("searchbox", name="Nombre").fill("test")

    print("then the user must see the message no products found")
    expect(page.get_by_text("no products found")).to_be_visible()

