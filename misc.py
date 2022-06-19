import re

class phone():

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

