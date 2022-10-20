from Entities.OrderProduct import OrderProduct
from Entities.Product import Product



def test_down_stock():
    # Arrange
    product1 = Product(1, "Water", 25, 20)

    order_product1 = OrderProduct()
    order_product1.add_product(product1, 10)

    # Assert
    assert product1.stock == 10