from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given the user opens the home page")
    page.goto("https://web-qa.dev.adalab.es/")

    print("When they visit the menu “About us”")
    page.get_by_role("link", name="Quiénes Somos").click()
    print("And they should see the title “About Us”")
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/about”](https://web-qa.dev.adalab.es/about”)")
    assert page.url == "https://web-qa.dev.adalab.es/about"


    print("When they visit the menu “Products”")
    page.get_by_role("link", name="Productos").click()
    print("And they should see the title “Product Catalog”")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    assert page.url == "https://web-qa.dev.adalab.es/products"

    print("When they visit the menu “Contact”")
    page.get_by_role("link", name="Contacto").click()
    print("And they should see the title “Contact Us”")
    expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    assert page.url == "https://web-qa.dev.adalab.es/contact"

    print("When they visit the menu “Home”")
    page.get_by_role("link", name="Inicio", exact=True).click()
    print("And they should see the title “Vida Verde”")
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/”](https://web-qa.dev.adalab.es/”)")
    assert page.url == "https://web-qa.dev.adalab.es/"
