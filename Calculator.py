def Addition(a, b):
    return a + b
def Subtraction(a, b):
    return a - b    
def Multiplication(a, b):
    return a * b
def Division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def Calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice(1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Addition of {num1} + {num2} = {Addition(num1, num2)}")

            elif choice == '2':
                print(f"Subtraction of {num1} - {num2} = {Subtraction(num1, num2)}")

            elif choice == '3':
                print(f" Multiplication of {num1} * {num2} = {Multiplication(num1, num2)}")

            elif choice == '4':
                print(f" Division of {num1} / {num2} = {Division(num1, num2)}")
            
           
        else:
            print("Invalid Input")
Calculator()