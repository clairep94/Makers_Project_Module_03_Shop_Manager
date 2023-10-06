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
            order = Order(row["id"], row["name"], row["unit_price"], row["stock_quantity"])
            orders.append(order)
        return orders

    # Find a single order by their id
    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["name"], row["unit_price"], row["stock_quantity"])

    # Find a single order by its name
    def find_id_by_name(self, name):
        name = name.lower()
        rows = self._connection.execute(
            'SELECT * from orders WHERE name = %s', [name])
        row = rows[0]
        return Order(row["id"], row["name"], row["unit_price"], row["stock_quantity"])

    # Create a new order
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, name, unit_price, stock_quantity):
        self._connection.execute('INSERT INTO orders ("name", "unit_price", "stock_quantity") VALUES (%s, %s, %s)', [
                                name, unit_price, stock_quantity])
        return self.find_id_by_name(name=name)

    # Delete an order by their id
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None

    # Update stock
    def update_stock_quantity(self, order_id, new_quantity:int):
        self._connection.execute(
            'UPDATE orders SET stock_quantity = %s WHERE id = %s', [new_quantity, order_id]
        )
        return None
    
    # Sell stock -- call for each order when order is created.
    def sell_order(self, order_id, sold_quantity:int):
        '''
        Params: order_id
        Return: total price of sale
        Side Effects: update db stock quantity 
        '''
        current_stock = self.find(order_id=order_id).stock_quantity
        if current_stock < sold_quantity:
            raise ValueError("Insufficient stock to sell.")
        
        # Update stock quantity
        new_stock_quantity = current_stock - sold_quantity
        self.update_stock_quantity(order_id=order_id, new_quantity=new_stock_quantity)
        
        # Return total price of units sold
        return sold_quantity * self.find(order_id=order_id).unit_price


    # Restock with additional units
    def restock_order(self, order_id, restock_quantity:int):
        current_stock = self.find(order_id=order_id).stock_quantity

        new_stock_quantity = current_stock + restock_quantity
        self.update_stock_quantity(order_id=order_id, new_quantity=new_stock_quantity)
        return None
