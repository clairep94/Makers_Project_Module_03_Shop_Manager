#TEMPLATE
from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order
from lib.order_repository import OrderRepository
import datetime
# from lib.orderitem_repository import OrderItemRepository

class Application():
    def __init__(self) -> None:
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

        self.item_repository = ItemRepository(self._connection)
        self.order_repository = OrderRepository(self._connection)

    def show_all_items(self):
        print('')
        items = self.item_repository.all() #list of all Item Objects
        items.sort(key=lambda x: x.id)
        for item in items:
            print(item)

    def show_all_orders(self):
        print("")
        orders = self.order_repository.all()
        orders.sort(key=lambda x: x.id)
        for order in orders:
            print(order)

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
                print('')
                print("Ok. Here are all the orders:")
                self.show_all_orders()

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

    def test_print(self): #COMMENT OUT ALL LATER
        obj1 = self.order_repository.all()[0]
        # obj1 = Order(1, 'First Customer', '2023-10-05', 5.50)
        # obj2 = Order(1, 'First Customer', '2023-10-05', 5.50)
        # print("Printing first order object with repr:")
        # print(obj1)
        # print("Date type:")
        # print(type(obj1.date))
        # print(obj1.date)
        # print(type(obj1.date.strftime('%Y-%m-%d')))
        # print(obj1.date.strftime('%Y-%m-%d'))
        # print(datetime.date(2023, 6, 27))
        # print(type(datetime.datetime.strptime('2023-10-05', '%Y-%m-%d').date()))
        # print(datetime.datetime.strptime('2023-10-05', '%Y-%m-%d').date())

        print("\nNow testing Create:")
        created_order = self.order_repository.create('Made-up Customer', datetime.date(2023,2,3), 30.99)
        expected_order = Order(3, 'Made-up Customer', datetime.date(2023,2,3), 30.99)
        print("Are they equal?")
        print(created_order == expected_order)

        print("EXPECTED:")
        print(f'''id:{expected_order.id} {type(expected_order.id)}
customer_name: {expected_order.customer_name} {type(expected_order.id)}
date: {expected_order.date} {type(expected_order.date)}
price: {expected_order.total} {type(expected_order.total)}''')

        print("ACTUAL:")
        print(f'''id:{created_order.id} {type(created_order.id)}
customer_name: {created_order.customer_name} {type(created_order.id)}
date: {created_order.date} {type(created_order.date)}
price: {created_order.total} {type(created_order.total)}''')


        # print("Printing Second order object with repr:")
        # print(obj2)
        # print(obj1 == obj2)

if __name__ == '__main__':
    app = Application()
    # app.run()
    app.test_print()