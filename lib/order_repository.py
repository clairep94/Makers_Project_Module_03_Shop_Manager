from lib.order import Order
from database_connection import DatabaseConnection

class OrderRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all orders
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            item = Order(row["id"], row["title"], row["release_year"], row["artist_id"])
            orders.append(item)
        return orders
    
    # Find a single order by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM orders WHERE id = %s', [id])
        row = rows[0]
        return Order(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new order
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, order:Order):
        self._connection.execute('INSERT INTO orders (title, release_year, artist_id) VALUES (%s, %s, %s)', [order.title, order.release_year, order.artist_id])
        return None

    # Delete an order by their id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [id]
        )
        return None
    

