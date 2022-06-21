from database import sql
from insert import insert
from misc import misc
from show import show

class modify(sql):
    def custUpdate(self):
        show().showCustomer()
        shift = 0
        numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to update : "))
            except:
                print("Only integers are allowed")

        fname, lname = input("Enter First and Last Name: ").split()
        phon = misc().input()
        Address = input("Enter Address: ")

        sqlString='UPDATE customer SET fname ="'+fname + '", lname = "' +lname+ '", phone ="' +phon+'", Address = "'+Address+'" WHERE id_customer ='+str(shift)+';'

        sql().modify(sqlString)
        show().showCustomer()


    def itemUpdate(self):
        show().showItems()
        shift = 0
        numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
        while not int(shift) in numLimit:
            try:
                shift = int(input("Please enter ID to update : "))
            except:
                print("Only integers are allowed")

        name = input("Food Name: ")
        Price = misc().getPrice()
        Type = insert().getval()
        Category = input("Category: ")

        sqlString='UPDATE items SET Name ="'+name +'", Price = "' +str(Price)+ '", Type ="' +Type+'", Category = "'+Category+'" WHERE id_item ='+str(shift)+';'
        sql().modify(sqlString)
        show().showItems()
