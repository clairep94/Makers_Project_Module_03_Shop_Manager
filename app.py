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
        if len(items) == 0:
            print("No items in database. Please created new items.")
        else:
            items.sort(key=lambda x: x.id)
            for item in items:
                print(item)


    def show_all_orders(self):
        print("")
        orders = self.order_repository.all()
        if len(orders) == 0:
            print("No orders in database. Please create new order.")
        else:
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
                print('')
                            
            #Create new item
            elif user_choice == "2":
                print('')
                new_item_name = input("What is the name of the item?\n>> ").lower()
                ##### 1) add error if typeerror ####
                new_item_price = round(float(input("What is the price of the item?\n>> ")), 2)
                ##### 2) add error if typeerror ####
                new_item_quantity = int(input("What is the stock quantity?\n>> "))
                ##### 3) add error if typeerror ####
                new_item = self.item_repository.create(name=new_item_name, unit_price=new_item_price, stock_quantity=new_item_quantity)
                print(f"Ok. Added new item:\n{new_item}.")

                self.show_all_items()
                print('')

            #Restock item
            elif user_choice == "3":
                print('')
                item_id = int(input("What is the item id?\n>> "))
                ##### 1) add error if order_id not found ####
                restock_quantity = int(input("What is the restock quantity?\n>> "))
                new_item = self.item_repository.find(item_id=item_id).name
                self.item_repository.restock_item(item_id=item_id, restock_quantity=restock_quantity)
                print(f"\nOk. Restocking item:\n{new_item}  +{restock_quantity} units.\n")
                
                self.show_all_items()
                print('')

            #List all orders
            elif user_choice == "4":
                print('')
                print("Ok. Here are all the orders:")
                self.show_all_orders()
                print('')

            #View order items
            elif user_choice == "5":
                print('')
                order_id = int(input("What is the order id?\n>> "))
                print('Finding order #{order_id}:\n')
                ##### self.show_order()

                ##### 1) add error if order_id not found ####
                ##### 2) Print all items for the order -- all items in orders_items for which order_id == order_id.
                    # EXAMPLE FORMAT:
                    # 
                    # Order #3: 
                    # John Doe - Placed on 2023-05-25 - Order Total: £40.25
                    # 
                    # #

                pass

            #Create order
            elif user_choice == "6":
                print("")
                customer_name = input("What is the name of the customer\n>> ")
                order_items_id_input = input("Please input all the item id's, separated by a space ' ' for your order.\nFor example, for 3 Apples, 2 Oranges, please put: 1 1 1 3 3")
                order_items_id = order_items_id_input.split(' ')
                #for each unique order id : order id --> name, number of times id is repeated in list, unit price, total price
                #for each entry in this dictionary, create an order_item object -- each item in the order gets a new order_item ID, and additional attribute of order ID

                #show order

                #show orders

            #Exit program.
            elif user_choice == "7":
                running = False

        # Exit message
        print("")
        print("Thanks for using the shop management program!")

    # def test_print(self): #COMMENT OUT ALL LATER
        # obj1 = self.order_repository.all()[0]
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

#         print("\nNow testing Create:")
#         created_order = self.order_repository.create('Made-up Customer', datetime.date(2023,2,3), 30.99)
#         expected_order = Order(3, 'Made-up Customer', datetime.date(2023,2,3), 30.99)
#         print("Are they equal?")
#         print(created_order == expected_order)

#         print("EXPECTED:")
#         print(f'''id:{expected_order.id} {type(expected_order.id)}
# customer_name: {expected_order.customer_name} {type(expected_order.id)}
# date: {expected_order.date} {type(expected_order.date)}
# price: {expected_order.total} {type(expected_order.total)}''')

#         print("ACTUAL:")
#         print(f'''id:{created_order.id} {type(created_order.id)}
# customer_name: {created_order.customer_name} {type(created_order.id)}
# date: {created_order.date} {type(created_order.date)}
# price: {created_order.total} {type(created_order.total)}''')

if __name__ == '__main__':
    app = Application()
    app.run()
    # app.test_print()