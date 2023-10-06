from lib.order import Order

class OrderRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all orders
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer_name"], row["date"], row["total"])
            orders.append(order)
        return orders

    # Find a single order by their id
    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["customer_name"], row["date"], row["total"])

    # Find a single order by its name
    def find_id_by_customer_name(self, customer_name):
        customer_name = customer_name.title()
        rows = self._connection.execute(
            'SELECT * from orders WHERE customer_name = %s', [customer_name])
        row = rows[0]
        return Order(row["id"], row["customer_name"], row["date"], row["total"])

    # Create a new order
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, customer_name, date, total):
        customer_name = customer_name.title()
        total = round(total,2)
        self._connection.execute('INSERT INTO orders ("customer_name", "date", "total") VALUES (%s, %s, %s)', [
                                customer_name, date, total])
        return self.find_id_by_customer_name(customer_name)

    # Delete an order by their id
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None

    # Update total
    def update_total(self, order_id, new_quantity:int):
        self._connection.execute(
            'UPDATE orders SET stock_quantity = %s WHERE id = %s', [new_quantity, order_id]
        )
        return None