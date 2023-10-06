from lib.item import Item

class ItemRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all items
    def all(self):
        rows = self._connection.execute('SELECT * from items')
        items = []
        for row in rows:
            item = Item(row["id"], row["name"], row["unit_price"], row["stock_quantity"])
            items.append(item)
        return items

    # Find a single item by their id
    def find(self, item_id):
        rows = self._connection.execute(
            'SELECT * from items WHERE id = %s', [item_id])
        row = rows[0]
        return Item(row["id"], row["name"], row["unit_price"], row["stock_quantity"])

    # Find a single item by its name
    def find_id_by_name(self, name):
        name = name.title()
        rows = self._connection.execute(
            'SELECT * from items WHERE name = %s', [name])
        row = rows[0]
        return Item(row["id"], row["name"], row["unit_price"], row["stock_quantity"])

    # Create a new item
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, name, unit_price, stock_quantity):
        name = name.title()
        unit_price = round(unit_price, 2)

        self._connection.execute('INSERT INTO items ("name", "unit_price", "stock_quantity") VALUES (%s, %s, %s)', [
                                name, unit_price, stock_quantity])
        return self.find_id_by_name(name=name)

    # Delete an item by their id
    def delete(self, item_id):
        self._connection.execute(
            'DELETE FROM items WHERE id = %s', [item_id])
        return None

    # Update stock
    def update_stock_quantity(self, item_id, new_quantity:int):
        self._connection.execute(
            'UPDATE items SET stock_quantity = %s WHERE id = %s', [new_quantity, item_id]
        )
        return None
    
    # Sell stock -- call for each item when order is created.
    def sell_item(self, item_id, sold_quantity:int):
        '''
        Params: item_id
        Return: total price of sale
        Side Effects: update db stock quantity 
        '''
        current_stock = self.find(item_id=item_id).stock_quantity
        if current_stock < sold_quantity:
            raise ValueError("Insufficient stock to sell.")
        
        # Update stock quantity
        new_stock_quantity = current_stock - sold_quantity
        self.update_stock_quantity(item_id=item_id, new_quantity=new_stock_quantity)
        
        # Return total price of units sold
        return sold_quantity * self.find(item_id=item_id).unit_price


    # Restock with additional units
    def restock_item(self, item_id, restock_quantity:int):
        current_stock = self.find(item_id=item_id).stock_quantity

        new_stock_quantity = current_stock + restock_quantity
        self.update_stock_quantity(item_id=item_id, new_quantity=new_stock_quantity)
        return None
