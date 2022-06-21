import re

class misc():

    def validPhone(self,number):
        phone_match = re.compile("^(\w{3}-\w{3}-\w{4})$")
        match = phone_match.match(number)
        if match:
            return match.groups(0)[0]
        return None

    def input(self):
        phone_number = ''
        while not self.validPhone(phone_number):
            phone_number = input("Enter phone number(format:###-###-####): ")
        return phone_number

    def ask_user(self):
        check = str(input("CONTINUE? (Y/N): ")).lower().strip()
        try:
                if check == 'y':
                    return check
                elif check == 'n':
                    return check
                else:
                    print('Invalid Input')
                    return self.ask_user()
        except Exception as error:
                print("Please enter valid inputs")
                print(error)
                return self.ask_user()

    def getPrice(self):
        Price = input("Price:")
        while True:
            try:
                Price = float(Price)
                break
            except:
                print("Only integers are allowed")
                Price = input("Price:")
        return "{:.2f}".format(Price)