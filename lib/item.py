class Item:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, unit_price, stock_quantity):
        self.id = id
        self.name = name.title()
        self.unit_price = round(unit_price,2)
        self.stock_quantity = stock_quantity


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Item
    def __repr__(self):
        return f"#{self.id} {self.name} - Unit Price: £{self.unit_price:.2f} - Quantity: {self.stock_quantity}"
