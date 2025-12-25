run = True
while(run):
    
    num1 = float(input("Enter the number 1: "))
    num2 = float(input("Enter the number 2: "))
    operator = input("Enter the operator(+,-,*,/): ")

    if operator == '+':
        print("Answer: ",num1 + num2)

    elif operator == '-':
        print("Answer: ",num1 - num2)

    elif operator == '*':
        print("Answer: ",num1 * num2)

    elif operator == '/':
        if num2 == 0:
            print("Zero can not be in denominator.")

        else:
            print("Answer: ",num1 / num2)

    else:
        print("Invalid")
    
    choice = input("Do you want to continue?(y/n)").lower()
    if choice == 'n':
        run = False