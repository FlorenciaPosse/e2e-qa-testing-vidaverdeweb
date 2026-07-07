from playwright.sync_api import Page
from pages.shopping_cart_page import ShoppingCart
from pages.menu_page import MenuPage
from pages.products_page import ProductsPage


def test_carrito(page: Page):

    products_page = ProductsPage(page)
    shopping_cart_page = ShoppingCart(page)
    menu_page = MenuPage(page)

    print("Given el usuario abre la página de productos")
    products_page.visit_products_page()
    

    print("When filtra por producto 'Regadera'")
    products_page.filter_by_name("regadera")
    

    print("And agrega el producto al carrito")
    products_page.add_product_to_shopping_cart("Regadera Metálica")

    print("And filtra por producto 'Tijeras'")
    products_page.filter_by_name("tijeras")
  

    print("And agrega el producto al carrito")
    products_page.add_product_to_shopping_cart("Tijeras de Podar")


    print("When visita el carrito")
    menu_page.visitShoppingCart()

    print("Then debe ver el producto Regadera y su precio")
    shopping_cart_page.verify_product_shopping_cart("Regadera Metálica")
    shopping_cart_page.verify_price_cart("24.00 €")
    
    print("And debe ver el producto Tijeras y su precio")
    shopping_cart_page.verify_product_shopping_cart("Tijeras de Podar")
    shopping_cart_page.verify_price_cart("18.50 €")

    print("And debe ver el resumen del pedido:")
    print("Subtotal:")
    shopping_cart_page.verify_price_cart("42.50 €")

    print("IVA 21%")
    shopping_cart_page.verify_price_cart("8.92 €")
  
    print("Envío")
    shopping_cart_page.verify_price_cart("5.00 €")
    print("Total")
    shopping_cart_page.verify_price_cart("56.42 €")


    print("When elimina el producto Regadera")
    shopping_cart_page.delete_product_cart("Regadera Metálica")

    print("Then no debe ver el producto Regadera")
    shopping_cart_page.verify_product_deleted_from_cart("Regadera Metálica")


    print("And ve resumen del pedido actualizado")
    print("Subtotal")
    shopping_cart_page.verify_price_cart("18.50 €")
    print("IVA 21%")
    shopping_cart_page.verify_price_cart("3.88 €")
    
    print("Envío")
    shopping_cart_page.verify_price_cart("5.00 €")
    print("total")
    shopping_cart_page.verify_price_cart("27.38 €")

    print("When vacía el carrito")
    shopping_cart_page.empty_cart()
    
    print("Then debe ver mensaje carrito vacío")
    shopping_cart_page.verify_empty_cart()

    print("And hace clic en Ver Productos")
    shopping_cart_page.view_products()

    print("Then debe ver la página de productos")
    products_page.verify_titol()
   