#TEMPLATE
from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item
# from lib.order_repository import OrderRepository
# from lib.order_item_repository import OrderItemRepository

class Application():
    def __init__(self) -> None:
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

    def run_again(self):
        print("")
        return input("Would you like to do something else? [y/n]\n\n>> ").upper() == "Y"

    def run(self):
        print("Welcome to the shop management program!\n")
        running = True

        while running == True: #While loop for run

            user_choice = input('''What would you like to do?

    1 = list all shop items
    2 = create a new item
    3 = restock item

    4 = list all orders
    5 = view order by order_number
    6 = create a new order

>> ''')

    #### PROGRAM FUNCTIONS ##### 
            
            #List all
            if user_choice == "1":
                print('')
                item_repository = ItemRepository(self._connection)
                items = item_repository.all() #list of all Item Objects
                for item in items:
                    print(str(item))
                
                if self.run_again() != True:
                    running = False
            
            #Create new item
            elif user_choice == "2":
                print('')
                item_repository = ItemRepository(self._connection)
                new_item = Item(None, "dish soap", 4.75, 20)
                item_repository.create(Item(None, "dish soap", 4.75, 20))


        # Exit message
        print("")
        print("Thanks for using the shop management program!")

if __name__ == '__main__':
    app = Application()
    app.run()