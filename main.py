from os import system
from insert import insert
from menu import menu

system('cls')
if __name__=='__main__':
    while(True):

        #menu().menu()
        option = ''
        try:
            menu().menu()
            option = int(input("please make a choice >>"))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            system('cls')
            menu().cusOption()
           
        elif option == 2:
            system('cls')
            menu().itemOption()

        elif option == 3:
            system('cls')
            menu().orderOption()

        elif option == 4:
            system('cls')
            insert().insertOrder()

        elif option == 5:
            print('Now exiting')
            exit()
        else:
            system('cls')
            print('Invalid option. Please enter a number between 1 and 5.')
