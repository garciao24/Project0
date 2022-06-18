import csv

#class with functions to create csv files based on the user input
class userInput():

    def customer(self,fname,lname,phone,Address):
        header = ['fname', 'lname', 'phone', 'Address']
        data = [
            [fname, lname, phone, Address]
            ]
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)

                 # write multiple rows
                writer.writerows(data)


    def items(self,Name,Price,Type,Category):
        header = ['Name', 'Price', 'Type', 'Category']
        data = [
            [Name, Price, Type, Category]
            ]
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)

                 # write multiple rows
                writer.writerows(data)


    def orders(self,id_orders,id_customer,id_item,OrderDate):
        header = ['id_orders', 'id_customer', 'id_item', 'orderDate']
        data = [
            [id_orders, id_customer, id_item, OrderDate]
            ]
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)

                 # write multiple rows
                writer.writerows(data)



