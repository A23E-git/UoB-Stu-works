def check_integer_sign():
    user_input = input("Enter an integer: ")
    
    try:
        
        number = int(user_input)
        
       
        if number > 0:
            print(f"{number} is a positive integer.")
        elif number < 0:
            print(f"{number} is a negative integer.")
        else:
            print("The number is zero.")
            
    except ValueError:
       
        print(f"Error: '{user_input}' is not a valid positive or negative integer.")


check_integer_sign()
