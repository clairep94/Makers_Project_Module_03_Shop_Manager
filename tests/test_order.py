from lib.order import Order
"""
Order constructs with an id, name and genre
"""
def test_order_constructs():
    order = Order(1, "John Doe", "2023-10-05", 10.25)
    assert order.id == 1
    assert order.customer_name == "John Doe"
    assert order.date == "2023-10-05"
    assert order.total == 10.25

"""
We can format orders to strings nicely
"""
def test_orders_format_nicely():
    order = Order(1, "John Doe", "2023-10-05", 10.50)
    assert str(order) == "#1 - Name: John Doe - Placed on: 2023-10-05 - Total: £10.50"
    # Try commenting out the `__repr__` method in lib/order.py
    # And see what happens when you run this test again.

"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, "John Doe", "2023-10-05", 10.50)
    order2 = Order(1, "John Doe", "2023-10-05", 10.50)
    assert order1 == order2
#     # Try commenting out the `__eq__` method in lib/order.py
#     # And see what happens when you run this test again.
