def addition():
    print("-" * 20)
    num1 = int(input("Enter 1st number: "))
    print("-" * 20)
    print(f"{num1} + ___ = ___")
    print("-" * 20)
    num2 = int(input("Enter 2nd number: "))
    print("-" * 20)
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    print("-" * 20)

def subtraction():
    print("-" * 20)
    num1 = int(input("Enter 1st number: "))
    print("-" * 20)
    print(f"{num1} - ___ = ___")
    print("-" * 20)
    num2 = int(input("Enter 2nd number: "))
    print("-" * 20)
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    print("-" * 20)
    
def multiplication():
    print("-" * 20)
    num1 = int(input("Enter 1st number: "))
    print("-" * 20)
    print(f"{num1} * ___ = ___")
    print("-" * 20)
    num2 = int(input("Enter 2nd number: "))
    print("-" * 20)
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    print("-" * 20)

def division():
    print("-" * 20)
    num1 = int(input("Enter 1st number: "))
    print("-" * 20)
    print(f"{num1} / ___ = ___")
    print("-" * 20)
    num2 = int(input("Enter 2nd number: "))
    print("-" * 20)
    if num2 == 0:
        print("Cannot divide by zero") 
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    print("-" * 20)
    

print("-" * 20)
print("Operations Available")
print("Type '1' for Addition")
print("Type '2' for Subtraction")
print("Type '3' for Multiplication")
print("Type '4' for Division")

chosen_operation = int(input("Enter operation option here: "))

if chosen_operation == 1:
    addition()
elif chosen_operation == 2:
    subtraction()
elif chosen_operation == 3:
    multiplication()
elif chosen_operation == 4:
    division()
else:
    print("-" * 20)
    print("Sorry that is not an available option. Please try again.")
    print("-" * 20)
