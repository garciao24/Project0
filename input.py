#placeholder




import csv

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = [
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA'],
#     ['American Samoa', 199, 'AS', 'ASM'],
#     ['Andorra', 468, 'AD', 'AND'],
#     ['Angola', 1246700, 'AO', 'AGO']
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)





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



    def items():
        pass
    def orders():
        pass


# inp = userInput()
# inp.customer("Steve","Jobbs","713-111-1111","nowhere 4321 st")
