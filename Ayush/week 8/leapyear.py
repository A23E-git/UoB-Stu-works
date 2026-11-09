import sys 
leap_year = input("Enter a year: ")
if leap_year.isdigit():
    leap_year = int(leap_year)
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        print("\033[32m{} is a leap year.\033[0m\n".format(leap_year))
    else:
        print("\033[31m{} is not a leap year.\033[0m\n".format(leap_year))
else:
    print("\033[31mInvalid year entered. Please enter a valid year.\033[0m\n")
sys.exit()