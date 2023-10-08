from lib.order_repository import OrderRepository
from lib.order import Order
import datetime
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
        Order(1, 'First Customer', datetime.date(2023,10,5), 5.50),
        Order(2, 'John Doe', datetime.date(2023,10,6), 14.50)
    ]

"""
When we call OrderRepository#find
We get a single Order object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(2)
    assert order == Order(2, 'John Doe', datetime.date(2023,10,6), 14.50)



"""
When we call OrderRepository#find_by_name
We get a single Order object reflecting the seed data.
"""
def test_get_id_by_customer_name(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    order = repository.find_id_by_customer_name("john doe")
    assert order == Order(2, 'John Doe', datetime.date(2023,10,6), 14.50)


"""
When we call OrderRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    
    created_order = repository.create('Made-up Customer', datetime.date(2023,2,3), 30.99)

    result = repository.all()
    assert result == [
        Order(1, 'First Customer', datetime.date(2023,10,5), 5.50),
        Order(2, 'John Doe', datetime.date(2023,10,6), 14.50),
        Order(3, 'Made-up Customer', datetime.date(2023,2,3), 30.99)
    ]
    assert created_order == Order(3, 'Made-up Customer', datetime.date(2023,2,3), 30.99)

"""
When we call OrderRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    repository.delete(2)
    result = repository.all()
    assert result == [
        Order(1, 'First Customer', datetime.date(2023,10,5), 5.50)
    ]
    

'''
When we call Order#update_total
We update the stock amount of the database
'''
def test_update_record(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    assert repository.find(1) == Order(1, 'First Customer', datetime.date(2023,10,5), 5.50)

    repository.update_total(1, 60)
    assert repository.find(1) == Order(1, 'First Customer', datetime.date(2023,10,5), 60.00)

