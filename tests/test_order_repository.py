from lib.order_repository import OrderRepository
from lib.order import Order

"""
When we call OrderRepository#all
We get a list of Order objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection) # Create a new OrderRepository

    orders = repository.all() # Get all Orders

    # Assert on the results
    assert orders == [
        Order(1, 'First Customer', '2023-10-05', 5.50),
        Order(2, 'John Doe', '2023-10-06', 14.50)
    ]

"""
When we call OrderRepository#find
We get a single Order object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(2)
    assert order == Order(2, 'John Doe', '2023-10-06', 14.50)



"""
When we call OrderRepository#find_by_name
We get a single Order object reflecting the seed data.
"""
def test_get_id_by_customer_name(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find_id_by_customer_name("john doe")
    assert order == Order(2, 'John Doe', '2023-10-06', 14.50)


"""
When we call OrderRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

#     created_order = repository.create("Made-up Customer", '2023-02-03', 30.99)

#     result = repository.all()
#     # assert result == [
#     #     Order(1, 'First Customer', '2023-10-05', 5.50),
#     #     Order(2, 'John Doe', '2023-10-06', 14.50),
#     #     Order(3, "Made-up Customer", '2023-02-03', 30.99)
#     # ]
#     assert created_order == Order(3, "Made-up Customer", '2023-02-03', 30.99)

# """
# When we call OrderRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/shop_manager.sql")
#     repository = OrderRepository(db_connection)

#     repository.delete(2)
#     result = repository.all()
#     assert result == [
#         Order(1, "apple", 1.00, 50),
#         Order(3, "orange", 2.75, 60),
#         Order(4, "pear", 3.50, 40),
#         Order(5, "lettuce", 2.00, 50),
#         Order(6, "bread", 3.00, 60)
#     ]
    

# '''
# When we call Order#update_stock
# We update the stock amount of the database
# '''
# def test_update_record(db_connection):
#     db_connection.seed("seeds/shop_manager.sql")
#     repository = OrderRepository(db_connection)
#     assert repository.find(2) == Order(2, "banana", 2.50, 50)

#     repository.update_stock_quantity(2, 60)
#     assert repository.find(2) == Order(2, "banana", 2.50, 60)

# def test_sell_stock(db_connection):
#     db_connection.seed("seeds/shop_manager.sql")
#     repository = OrderRepository(db_connection)
#     assert repository.find(2) == Order(2, "banana", 2.50, 50)

#     assert repository.sell_order(2, 3) == 7.50
#     assert repository.find(2) == Order(2, "banana", 2.50, 47)

# def test_restock_order(db_connection):
#     db_connection.seed("seeds/shop_manager.sql")
#     repository = OrderRepository(db_connection)
#     assert repository.find(2) == Order(2, "banana", 2.50, 50)
#     repository.restock_order(2, 40)
#     assert repository.find(2) == Order(2, "banana", 2.50, 90)
