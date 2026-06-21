from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given the user opens the products page")
    page.goto("https://web-qa.dev.adalab.es/products")
    
    print("When they filter by product “Regadera”")
    page.get_by_placeholder("Buscar productos...").fill("Regadera")
    page.get_by_role("img", name="Regadera Metálica").click()
    print("And they add the product to the cart")
    page.get_by_label("Añadir Regadera Metálica al").click()
    
    print("And they filter by product “Tijera”")
    page.get_by_placeholder("Buscar productos...").fill("tijeras")
    page.get_by_role("img", name="Tijeras de Podar").click()
    page.get_by_label("Añadir Tijeras de Podar al").click()
    print("And they add the product to the cart")
    
    print("When they view the cart by clicking the cart icon")
    page.get_by_role("link", name="Carrito de compra").click()
    
    print("Then they should see the product “Regadera”")
    expect(page.get_by_text("HerramientasRegadera Metálica24.00 €Eliminar")).to_be_visible()

    print("And they should see its price “24”")
    expect(page.get_by_text("24.00 €")).to_be_visible()
        
    print("And they should see the product “Tijeras”")
    expect(page.get_by_text("HerramientasTijeras de Podar18.50 €Eliminar")).to_be_visible()

    print("And they should see its price “18.50”")
    expect(page.get_by_text("18.50 €")).to_be_visible()
    
    print("And they should see the order summary with subtotal “42.50”")
    expect(page.get_by_text("Productos (2)42.50 €")).to_be_visible()
    
    print("And VAT 21% “8.92”")
    expect(page.get_by_text("IVA (21%)8.92 €")).to_be_visible()
    
    print("And shipping “5”")
    expect(page.get_by_text("Envío5.00 €")).to_be_visible()
    
    print("And the total “56.42”")
    expect(page.get_by_text("Total56.42 €")).to_be_visible()

    print("When they remove the product “Regadera”")
    page.get_by_label("Eliminar Regadera Metálica").click()
    
    print("Then they should not see the product “Regadera”")
    expect(page.get_by_text("HerramientasRegadera Metálica24.00 €Eliminar")).not_to_be_visible()

    print("And the updated order summary with subtotal “18.50”")
    expect(page.get_by_text("Productos (1)18.50 €")).to_be_visible()
    
    print("And VAT updated to “3.88”")
    expect(page.get_by_text("IVA (21%)3.88 €")).to_be_visible()

    print("And shipping “5”")
    expect(page.get_by_text("Envío5.00 €")).to_be_visible()


    print("And the total “27.38”")
    expect(page.get_by_text("Total27.38 €")).to_be_visible()


    print("When they empty the cart")
    page.get_by_role("button", name="Vaciar Carrito").click()

    print("Then they should not see the product “Tijeras”")
    expect(page.get_by_text("Carrito de CompraTu carrito")).to_be_visible()

    print("And they should see the message “cart empty”")
    expect(page.get_by_text("Tu carrito está vacío")).to_be_visible()
    
    print("And they click on “view products”")
    page.get_by_role("link", name="Productos", exact=True).click()

    print("And they should see the products page")
    expect(page.locator("div").filter(has_text="Catálogo de ProductosExplora")).to_be_visible()


