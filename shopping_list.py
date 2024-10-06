shopping_list = []

def add_to_list():
    pass

def remove_from_list():
    pass

def print_list():
    pass

program_on = True

while program_on:
    print("Options Available:")
    print("Type '1' to add to list")
    print("Type '2' to remove from list")
    print("Type '3' to print the list")
    print("Type '4' to quit")

    option_number = int(input("Type option here: "))

    if option_number == 1:
        add_to_list()
    elif option_number == 2:
        remove_from_list()
    elif option_number == 3:
        print_list()
    elif option_number == 4:
        program_on = False
    else:
        print("Sorry that option is not available.\nTry again.")
    
