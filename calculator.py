def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def subtract(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")
    
def multiply(a, b):
    answer = a * b
    print(f"{a} x {b} = {answer}")

def divide(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")


def print_menu():
    print("""
    What do you want to do?
    (a) Addition
    (b) Subtraction
    (c) Multiplication
    (d) Division
    (e) Exit
    """)

done = False

while not done:
    print_menu()
    choice = input("Enter your choice: ")

    match choice.lower():

        case "a":
            print("Addition")
            a = int(input("Input the first number: "))
            b = int(input("Input the second number: "))
            add(a,b)

        case "b":
            print("Subtraction")
            a = int(input("Input the first number: "))
            b = int(input("Input the second number: "))
            subtract(a,b)

        case "c":
            print("Multiply")
            a = int(input("Input the first number: "))
            b = int(input("Input the second number: "))
            multiply(a, b)

        case "d":
            print("Divide")
            a = int(input("Input the first number: "))
            b = int(input("Input the second number: "))
            divide(a, b)
        
        case "e":
            print("Thanks for using the calculator")
            done = True
        
        case _:
            print("Invalid choice")