shopping_list = []

def add_to_list():
    print("-" * 50)
    item = input("What item would you like to add?\n")
    if item in shopping_list:
        print(f"That {item} is already on your list.")
    else:
        shopping_list.append(item)
        print(f"{item} has been added to your list.")
    print("-" * 50)

def remove_from_list():
    print("-" * 50)
    item = input("What item would you like to remove?\n")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your list.")
    else:
        print(f"{item} doesn't exist on your list.")
    print("-" * 50)

def print_list():
    print("-" * 50)
    print("These are the items on your list:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print("-" * 50)

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
        print("-" * 50)
        print("Goodbye!")
        program_on = False
    else:
        print("Sorry that option is not available.\nTry again.")
    