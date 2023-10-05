class Order:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, customer_name, date, total) -> None:
        self.id = id
        self.customer_name = customer_name
        self.date = date
        self.total = round(total, 2)
    
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__
    def __eq__(self, other):
        if isinstance(other, Order):
            return (self.id == other.id and
                    self.customer_name == other.customer_name and
                    self.date == other.date and
                    self.total == other.total)
        return False

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"#{self.id} - Name: {self.customer_name} - Placed on: {self.date} - Total: £{self.total:.2f}"

