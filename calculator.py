while True:
    print("OPTIONS")
    print("Enter '+' for Addition ")
    print("Enter '-' for Subtraction ")
    print("Enter '*' for Multiplication ")
    print("Enter '/' for Division ")
    print("Enter 'N' to end program")
    userInput = input(": ").upper()

    if userInput == 'N':
        print("End of Program")
        break
    elif userInput in ["+", "-", "*", "/"]:
        num1 = float(input("Enter Num1: "))
        num2 = float(input("Enter Num2: "))

        if userInput == "+":
            result = num1 + num2
        elif userInput == "-":
            result = num1 - num2
        elif userInput == "*":
            result = num1 * num2
        else:
            if num2 != 0:
                result = num1/num2
            else:
                print("Cannot be divided")
            continue
        print("Result: ", result)

    else:
        print("Invalid respone")


