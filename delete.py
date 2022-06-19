from operator import delitem
from database import sql
from misc import misc
from show import show

class delete(sql):

    def warning(self):
        print("!!!WARNING!!! DELETING WILL ALSO DELETE ANYTHING ASSSOCIATED WITH IT")
        return misc().ask_user()

    def delCustomer(self):
        strt = self.warning()
        if strt == 'n':
            return
        show().showCustomer()
        shift = 0
        numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to delete : "))
            except:
                print("Only integers are allowed")
        sqlString1="DELETE FROM orders WHERE id_customer ="+str(shift)+';'
        sqlString2="DELETE FROM customer WHERE id_Customer = "+str(shift)+';'
        sqlString = sqlString1+sqlString2
        sql().modify(sqlString)
        show().showCustomer()
    
    def delItems(self):
        strt = self.warning()
        if strt == 'n':
            return
        show().showItems()
        shift = 0
        numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to delete : "))
            except:
                print("Only integers are allowed")

        sqlString1="DELETE FROM orders WHERE id_item = "+str(shift)+';'
        sqlString2="DELETE FROM items WHERE id_item ="+str(shift)+';'
        sqlString=sqlString1+sqlString2
        sql().modify(sqlString)
        show().showItems()


    def delOrders(self):
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
