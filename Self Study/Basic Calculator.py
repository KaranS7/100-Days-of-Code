while True:
    print("Welcome to calculator program\n")
    
    number1 = float(input("Please input first number\n"))
    number2 = float(input("Please input second number\n"))
    operator = input("Please select your operation: \n1 for Add \n2 for Subtract \n3 for Multiply\n4 for Divide\n").lower()
    
    number3 = float(number1)
    number4 = float(number2)
    
    a = number3 + number4
    s = number3 - number4
    m = number3 * number4
    d = number3 / number4
    
    if operator == "1":
        print(f"The addition of {number1} and {number2} is {a:.2f}")
    elif operator == "2":
        print(f"The subtraction of {number1} and {number2} is {s:.2f}")
    elif operator == "3":
        print(f"The multiplication of {number1} and {number2} {m:.2f}")
    elif operator == "4":
        print(f"The division of {number1} and {number2} {d:.2f}")
    else:
        print("You have selected a wrong input")
        
    choice = input("Do you want to run another calculation? \nY for Yes and N for No\n").lower()
    if choice == "n":
        print("Thank you for using this program")
        break