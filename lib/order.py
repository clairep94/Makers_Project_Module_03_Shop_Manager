class Order:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    # Note that each Order obj is initialise with sql date datatypes in the 'date' column.
    def __init__(self, id, customer_name, sql_date_obj, total):
        self.id = id
        self.customer_name = customer_name.title()
        self.date = sql_date_obj #date object
        self.total = float(round(total,2)) #convert from decimal.decimal to float


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Order
    def __repr__(self):
        return f"#{self.id} {self.customer_name} - Ordered on: {self.date} - Order Total: £{self.total:.2f}"
