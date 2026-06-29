from playwright.sync_api import Page, expect

def test_checkout_purchase_with_valid_data(page: Page):
    print("Given the user is on the products page")
    page.goto("https://web-qa.dev.adalab.es/products")
    
    print('And filters products by the name "palas"')
    page.get_by_placeholder("Buscar productos...").fill("palas")
    expect(page.get_by_text("Juego de Palas")).to_be_visible()

    print("And adds the product to the cart")
    page.get_by_text("Añadir al carrito").first.click()
    
    print('And clicks on "Finalizar compra"')
    page.get_by_text("Finalizar compra").first.click()
    expect(page.get_by_text("Resumen del pedido")).to_be_visible()

    print('And clicks on "Proceder al pago"')
    page.get_by_text("Proceder al pago").first.click()

    print('Then the order summary should display the product "Juego de Palas"')
    expect(page.get_by_text("Juego de Palas")).to_be_visible()
   
    print('And the product price should be "15.99"')
    expect(page.get_by_text("15.99").first).to_be_visible()

    print('And the subtotal should be "15.99"')
    expect(page.get_by_text("15.99").last).to_be_visible()

    print('And the VAT should be "3.36"')
    expect(page.get_by_text("3.36")).to_be_visible()

    print('And the shipping cost should be "5.00"')
    expect(page.get_by_text("5.00")).to_be_visible()

    print('And the total amount should be "24.35"')
    expect(page.get_by_text("24.35").first).to_be_visible()

    print('When the user enters the name "Reyes Maria"')
    page.get_by_label("Nombre Completo").fill("Reyes Maria")

    print('And enters the email "test@gmail.com"')
    page.get_by_label("Email").fill("test@gmail.com")

    print('And enters the address "Málaga, Calle Larios, 25"')
    page.get_by_label("Dirección").fill("Málaga, Calle Larios, 25")

    print('And enters a valid card number')
    page.get_by_label("Número de tarjeta de crédito").fill("4242 4242 4242 4242")

    print('And clicks on "Completar compra"')
    page.get_by_role("button", name="Completar compra").click()

    print('Then the user should see the message "Compra realizada con éxito"')
    expect(page.get_by_text("Compra realizada con éxito")).to_be_visible()

    print('And the total amount should be "24.35"')
    expect(page.get_by_text("24.35")).to_be_visible()

    print('When the user clicks on "Ir al inicio"')
    page.get_by_text("Ir al inicio").first.click()

    print("Then the user should be redirected to the home page")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/")
