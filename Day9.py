
#This program will take user input for a number and catch errors if the user inputs something invalid (non-integer).
print("Please enter the following information")

while True:
    name = input("Please enter your name: ")
    cap_name = name.capitalize()
    if name.isalpha():
        break
    else:
        print("Invalid input. Only letters are allowed.")

while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
print(f"Your name is {cap_name}, and your age is {age}")

#Code by Ohene Caleb