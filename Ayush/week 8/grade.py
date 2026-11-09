import sys
student_grade = input("Enter your grade: ")
if student_grade.isdigit():
    student_grade = float(student_grade)
    if 70 <= student_grade <= 100:
        print("\033[32mYou got a 1st\033[0m\n")
    elif 60 <= student_grade < 69:
        print("\033[33mYou got a 2:1\033[0m\n")
    elif 50 <= student_grade < 59:
        print("\033[33mYou got a 2:2\033[0m\n")
    elif 40 <= student_grade < 49:
        print("\033[33mYou got a 3rd\033[0m\n")
    elif 0 <= student_grade < 39:
        print("\033[31mYou failed\033[0m\n")
else:
    print("\033[31mInvalid grade entered. Please enter a grade between 0 and 100.\033[0m\n")

sys.exit()
