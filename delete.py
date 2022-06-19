

from operator import delitem
from database import sql
from show import show


class delete(sql):
    def delCustomer(self):
        show().showCustomer()
        shift = 0
        numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to delete : "))
            except:
                print("Only integers are allowed")
        sqlString="DELETE FROM customer WHERE id_Customer = "+str(shift)
        #print(sqlString)
        sql().modify(sqlString)
        show().showCustomer()

    
    def delItems(self):
        show().showItems()
        shift = 0
        numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to delete : "))
            except:
                print("Only integers are allowed")

        sqlString="DELETE FROM items WHERE id_item = "+str(shift)
        #print(sqlString)
        sql().modify(sqlString)
        show().showItems()

    def delOrders(self):#orders in progress
        show().showOrders()
        shift = 0
        numLimit = sql().query("SELECT id_orders FROM orders ORDER BY id_orders ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to delete : "))
            except:
                print("Only integers are allowed")
        sqlString="DELETE FROM orders WHERE id_orders = "+str(shift)
        #print(sqlString)
        sql().modify(sqlString)
        show().showOrders()


