from lib.item_repository import ItemRepository
from lib.item import Item

"""
When we call ItemRepository#all
We get a list of Item objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ItemRepository

    items = repository.all() # Get all Items

    # Assert on the results
    assert items == [
        Item(1, "apple", 1.00, 50),
        Item(2, "banana", 2.50, 50),
        Item(3, "orange", 2.75, 60),
        Item(4, "pear", 3.50, 40),
        Item(5, "lettuce", 2.00, 50),
        Item(6, "bread", 3.00, 60)
    ]

"""
When we call ItemRepository#find
We get a single Item object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(3)
    assert item == Item(3, "orange", 2.75, 60)

"""
When we call ItemRepository#find
We get a single Item object reflecting the seed data.
"""
def test_get_single_record2(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(2)
    assert item == Item(2, "banana", 2.50, 50)


"""
When we call ItemRepository#find
We get a single Item object reflecting the seed data.
"""
def test_get_single_record3(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find(1)
    assert item == Item(1, "apple", 1.00, 50)


"""
When we call ItemRepository#find_by_name
We get a single Item object reflecting the seed data.
"""
def test_get_id_by_name(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    item = repository.find_id_by_name("orange")
    assert item == Item(3, "orange", 2.75, 60)


"""
When we call ItemRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    created_item = repository.create("dish soap", 4.75, 20)

    result = repository.all()
    assert result == [Item(1, "apple", 1.00, 50),
        Item(2, "banana", 2.50, 50),
        Item(3, "orange", 2.75, 60),
        Item(4, "pear", 3.50, 40),
        Item(5, "lettuce", 2.00, 50),
        Item(6, "bread", 3.00, 60),
        Item(7, "dish soap", 4.75, 20)
    ]
    assert created_item == Item(7, "dish soap", 4.75, 20)

"""
When we call ItemRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    repository.delete(2)
    result = repository.all()
    assert result == [
        Item(1, "apple", 1.00, 50),
        Item(3, "orange", 2.75, 60),
        Item(4, "pear", 3.50, 40),
        Item(5, "lettuce", 2.00, 50),
        Item(6, "bread", 3.00, 60)
    ]
    

'''
When we call Item#update_stock
We update the stock amount of the database
'''
def test_update_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    assert repository.find(2) == Item(2, "banana", 2.50, 50)

    repository.update_stock_quantity(2, 60)
    assert repository.find(2) == Item(2, "banana", 2.50, 60)

def test_sell_stock(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    assert repository.find(2) == Item(2, "banana", 2.50, 50)

    assert repository.sell_item(2, 3) == 7.50
    assert repository.find(2) == Item(2, "banana", 2.50, 47)

def test_restock_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    assert repository.find(2) == Item(2, "banana", 2.50, 50)
    repository.restock_item(2, 40)
    assert repository.find(2) == Item(2, "banana", 2.50, 90)
