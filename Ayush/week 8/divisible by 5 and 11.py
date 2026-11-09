import sys
enter_number = input("Enter a number: ")
if enter_number.isdigit():
    enter_number = int(enter_number)
    if enter_number % 5 == 0 and enter_number % 11 == 0:
        print("\033[32m{} is divisible by both 5 and 11.\033[0m\n".format(enter_number))
    elif enter_number % 5 == 0:
        print("\033[33m{} is divisible by 5 but not by 11.\033[0m\n".format(enter_number))
    elif enter_number % 11 == 0:
        print("\033[33m{} is divisible by 11 but not by 5.\033[0m\n".format(enter_number))
    else:
        print("\033[31m{} is not divisible by either 5 or 11.\033[0m\n".format(enter_number))
else:
    print("\033[31mInvalid input. Please enter a valid integer.\033[0m\n")
sys.exit()