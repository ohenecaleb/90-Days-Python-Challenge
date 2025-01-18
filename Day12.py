import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def print_values(data, keys):
    for key in keys:
        if key in data:
            print(f"{key}: {data[key]}")
        else:
            print(f"{key} not found in the JSON data.")

if __name__ == "__main__":
    file_path = input("Enter the path to the JSON file: ")
    data = read_json(file_path)
    
    keys = input("Enter the keys you want to retrieve, separated by commas: ").split(',')
    keys = [key.strip() for key in keys]
    
    print_values(data, keys)