from lib.order import Order
import datetime

"""
Order constructs with an id, customer_name, date, total
"""
def test_order_constructs():
    order = Order(1, "John Doe", datetime.date(2024,10,25), 45.40)
    assert order.id == 1
    assert order.customer_name == "John Doe"
    assert order.date == datetime.date(2024,10,25)
    assert order.total == 45.40


"""
We can format orders to strings nicely
"""
def test_orders_format_nicely():
    order = Order(1, "John Doe", datetime.date(2024,10,25), 45.40)
    assert str(order) == "#1 John Doe - Ordered on: 2024-10-25 - Order Total: £45.40"
    # Try commenting out the `__repr__` method in lib/order.py
    # And see what happens when you run this test again.

"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, "John Doe", datetime.date(2024,10,25), 45.40)
    order2 = Order(1, "John Doe", datetime.date(2024,10,25), 45.40)
    assert order1 == order2
#     # Try commenting out the `__eq__` method in lib/order.py
#     # And see what happens when you run this test again.

