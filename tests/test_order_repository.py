from lib.order_repository import OrderRepository
from lib.order import Order

"""
When we call OrderRepository#all
We get a list of Order objects reflecting the seed data.
"""
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
#     repository = OrderRepository(db_connection) # Create a new OrderRepository

#     orders = repository.all() # Get all orders
#     expected_total = round(14.50, 2)
#     assert orders[1] == Order(2, 'John Doe', '2023-10-06', expected_total)
    
"""
When we call OrderRepository#find
We get a single Order object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(1)
    assert order == Order(1, "First Customer", "2023-10-05", 5.50)

# """
# When we call OrderRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = OrderRepository(db_connection)

#     repository.create(Order(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Order(1, "Pixies", "Rock"),
#         Order(2, "ABBA", "Pop"),
#         Order(3, "Taylor Swift", "Pop"),
#         Order(4, "Nina Simone", "Jazz"),
#         Order(5, "The Beatles", "Rock"),
#     ]

# """
# When we call OrderRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = OrderRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Order(1, "Pixies", "Rock"),
#         Order(2, "ABBA", "Pop"),
#         Order(4, "Nina Simone", "Jazz"),
#     ]
