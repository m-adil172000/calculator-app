
from calcfun import do_addition, do_subtraction, do_division

def main():
    print("Welcome to the calculator App")
    print("""
          \nSelect the function from the following options:
          1. Add
          2. Subtract
          3. Divide
          """)

    user_input = input("Select the function: ")
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))


    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "3":
        result = do_division(a,b)
    else:
        result = do_subtraction(a,b)
    
    print('Result: ',result)


if  __name__ == "__main__":
    main()