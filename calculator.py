def divide(num1, num2):
    return num1 / num2

def subtraction(num1, num2):
    return num1 - num2

def addition(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

while True:
    try:
        decision = int(input("""\nWould you like to:
    Option 1: Use the calculator
    Option 2: View the equations.
    Type 1 or 2 to choose: 
    """))
        #choosing a number that has no option, must choose again
        if decision != 1 and decision != 2:         
            print("Invalid input. Only type '1' or '2'.")

        if decision == 1:
            quit = False
            #gives user oportunity to leave the calculator later
            while quit == False:
                try:
                    num1 = float(input("Please input the first number you would like to do a calculation with: "))
                    num2 = float(input("Please enter the second number: "))

                #if input couldn't be converted to a float it had non-digits
                except ValueError:      
                    print("That wasn't a valid number! Please enter a numerical value.")
                    continue

                operator = input("""Choose from the list of operators below:
                /
                -
                +
                *
                """)
                #if valid operator, do corresponding function
                if operator in ("/", "-", "+", "*"):        
                    if operator == "/":
                        #prevent user from dividing by 0
                        if num2 == 0:
                            print("")
                        else:
                            equation = f"{num1} {operator} {num2} = {divide(num1, num2)}"
                    if operator == "-":
                        equation = f"{num1} {operator} {num2} = {subtraction(num1, num2)}"
                    if operator == "+":
                        equation = f"{num1} {operator} {num2} = {addition(num1, num2)}"
                    if operator == "*":
                        equation = f"{num1} {operator} {num2} = {multiply(num1, num2)}"
                    try: 
                        print(equation)
                    #if user tried to /0, equation will not be defined and will return NameError
                    except NameError:
                        print("Sorry we couldn't do that equation!")
                        break
                    
                    #append to file
                    with open("equations.txt", "a") as f:   
                        f.write(f"{equation}\n")
                    user_quit = input("\nWould you like to quit the calculator? Please type quit if you do, or hit enter if you don't.").lower()
                    if user_quit == "quit":
                        quit = True

                else:
                    print("Not a valid operator. Please try again.")

        if decision == 2:
            file = input("Please enter the file name: ")
            f = None
            try:
                #if the user hasn't added.txt to the end, still accept as valid name
                #add.txt to the end to make valid name
                if file.find(".txt") == -1:     
                    f = open(f"{file}.txt", "r")    
                    contents = f.read()
                    print(contents)
                else:
                    f = open(f"{file}", "r")
                    contents = f.read()
                    print(contents)
            
            #if file does not exist, "r" type will return this error instead of creating file
            except FileNotFoundError:      
                print("Sorry this file cannot be found.")
            finally:
                if f is not None:
                    f.close()


    except ValueError:
        print("Invalid input. Only type '1' or '2'.")
