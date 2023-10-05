from lib.item import Item

"""
Item constructs with an id, name, stock_quantity, unit_price
"""
def test_item_constructs():
    item = Item(1, "Apple", 1.00, 50)
    assert item.id == 1
    assert item.name == "Apple"
    assert item.stock_quantity == 50
    assert item.unit_price == 1.00


"""
We can format items to strings nicely
"""
def test_items_format_nicely():
    item = Item(1, "Apple", 1.00, 50)
    assert str(item) == "#1 Apple - Unit Price: £1.00 - Quantity: 50"
    # Try commenting out the `__repr__` method in lib/item.py
    # And see what happens when you run this test again.

"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, "Apple", 1.00, 50)
    item2 = Item(1, "Apple", 1.00, 50)
    assert item1 == item2
    # Try commenting out the `__eq__` method in lib/item.py
    # And see what happens when you run this test again.

