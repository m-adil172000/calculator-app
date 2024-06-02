
from calcfun import do_addition, do_subtraction
from area import calculate_area


def main():
    print("Welcome to the calculator App")
    print("""
          \nSelect the function from the following options:
          1. Add
          2. Subtract
          3. Area
          """)

    user_input = input("Select the function: ")
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))


    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "3":
        result = calculate_area(a,b)
    else:
        result = do_subtraction(a,b)
    
    print('Result: ',result)


if  __name__ == "__main__":
    main()