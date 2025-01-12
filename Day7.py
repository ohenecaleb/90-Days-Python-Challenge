def main():
    user_info = {}

    while True:
        print("1. Add user information")
        print("2. Retrieve user information")
        print("3. Exit")
        option = input("Enter your option1: ")

        if option == '1':
            name = input("Enter name: ").capitalize()
            age = input("Enter age: ")
            user_info[name] = age
            print(f"Information for {name} added.\n")
        elif option == '2':
            name = input("Enter name to retrieve: ").capitalize()
            if name in user_info:
                print(f"Name: {name}, Age: {user_info[name]}\n")
            else:
                print(f"No information found for {name}.\n")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()