import random 
integer1,interger2 = input("Enter two integers separated by a space: ").split()
random_number = random.randint(int(integer1), int(interger2))
print(random_number)