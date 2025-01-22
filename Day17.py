import requests

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")
    content = fetch_webpage(url)
    print(content)