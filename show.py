from collections import deque
from database import sql
from tabulate import tabulate

class show(sql):

    def showCustomer(self):
        self.cursor.execute("SELECT * FROM customer")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["Customer ID", "FirstName", "LastName", "Phone", "Address"],tablefmt="fancy_grid"))

    def showItems(self):
        self.cursor.execute("SELECT * FROM items")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["Item ID", "Name", "Price", "Type", "Category"],tablefmt="fancy_grid"))

    def showOrders(self):
        self.cursor.execute("""SELECT orders.id_orders, orders.OrderDate , customer.fname, customer.lname, items.Name, items.Price
                            FROM pizzaria.orders 
                            JOIN customer ON orders.id_customer = customer.id_Customer 
                            JOIN items ON orders.id_item = items.id_item""")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["ID Orders", "Order Date" , "Customer fname", "Customer lname", "Food Item" , "Price"],tablefmt="fancy_grid"))


