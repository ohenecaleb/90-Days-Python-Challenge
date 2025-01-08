#Data Types and Variables

#Creating a variable to accept name and age from users
name = input("Enter your name: ")
age = input("Enter your age: ")
DOB = 2021 - int(age)
#Printing the name and age of the user
print("Hello " + name + "! Your date of birth is " + str(DOB) )
