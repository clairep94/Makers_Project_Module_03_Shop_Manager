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

        self.item_repository = ItemRepository(self._connection)

    def show_all_items(self):
        print('')
        items = self.item_repository.all() #list of all Item Objects
        items.sort(key=lambda x: x.id)
        for item in items:
            print(str(item))

    def run(self):
        print("Welcome to the shop management program!\n")
        running = True
        
        while running == True: #While loop for run

            user_choice = input('''
>> What would you like to do?

    1 = list all shop items
    2 = create a new item
    3 = restock item

    4 = list all orders
    5 = view order items
    6 = create a new order
    7 = exit program

>> ''')

    #### PROGRAM FUNCTIONS ##### 

            #List all
            if user_choice == "1":
                print('')
                print("Ok. Here are all the items:")
                self.show_all_items()
                            
            #Create new item
            elif user_choice == "2":
                print('')
                new_item_name = input("What is the name of the item?\n>> ").lower()
                new_item_price = round(float(input("What is the price of the item?\n>> ")), 2)
                new_item_quantity = int(input("What is the stock quantity?\n>> "))

                new_item = self.item_repository.create(name=new_item_name, unit_price=new_item_price, stock_quantity=new_item_quantity)
                print(f"Ok. Added new item:\n{new_item}.")

                self.show_all_items()

            #Restock item
            elif user_choice == "3":
                print('')
                item_id = int(input("What is the item id?\n>> "))
                restock_quantity = int(input("What is the restock quantity?\n>> "))

                self.item_repository.restock_item(item_id=item_id, restock_quantity=restock_quantity)
                print(f"Ok. Restocked item:\n{new_item}.")
                
                self.show_all_items()


            #List all orders
            elif user_choice == "4":
                pass

            #View order items
            elif user_choice == "5":
                pass

            #Create order
            elif user_choice == "6":
                pass

            #Exit program.
            elif user_choice == "7":
                running = False

        # Exit message
        print("")
        print("Thanks for using the shop management program!")

if __name__ == '__main__':
    app = Application()
    app.run()