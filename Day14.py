import requests

def fetch_github_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        return None

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    user_profile = fetch_github_user_profile(username)
    
    if user_profile:
        print(f"User: {user_profile['login']}")
        print(f"Name: {user_profile['name']}")
        print(f"Company: {user_profile['company']}")
        print(f"Location: {user_profile['location']}")
        print(f"Public Repos: {user_profile['public_repos']}")
        print(f"Followers: {user_profile['followers']}")
        print(f"Following: {user_profile['following']}")
    else:
        print("User not found or an error occurred.")