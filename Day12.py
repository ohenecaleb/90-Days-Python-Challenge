#Program to read a JSON file and print specific values
import json
import sys

#Function to read a JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

#Function to print specific values from the JSON data
def print_values(data, keys):
    for key in keys:
        if key in data:
            print(f"{key}: {data[key]}")
        else:
            print(f"{key} not found in the JSON data.")

#Main code
if __name__ == "__main__":
    while True: # Loop until a valid file path is entered
        try:
            file_path = input("Enter the path to the JSON file (or type 'exit' to quit): ")
            if file_path.lower() == 'exit':
                print("Exiting program.")
                sys.exit() # Exit the program
            data = read_json(file_path)
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
           

    keys = input("Enter the keys you want to retrieve, separated by commas: ").split(',')
    keys = [key.strip() for key in keys]# Remove any leading/trailing whitespaces
    
    print_values(data, keys)
    
#Code By Ohene Caleb
