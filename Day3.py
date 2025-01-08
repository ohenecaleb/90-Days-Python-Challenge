#Conditional Statements
# if, elif, else

# Example 1, a simple app to verify the eligiblity of a user to vote

# Asking the user for their age
age = int(input("Enter your age: "))

# Checking if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are ineligible to vote.")