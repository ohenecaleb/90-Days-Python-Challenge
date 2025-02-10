import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_password(hash_to_crack, wordlist_file):
    with open(wordlist_file, 'r') as file:
        for line in file:
            word = line.strip()
            if hash_password(word) == hash_to_crack:
                print(f"Password found: {word}")
                return word
    print("Password not found in wordlist.")
    return None

if __name__ == "__main__":
    hash_to_crack = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddc8a3f6d9f6f6f6f6f"  # Example hash for 'password'
    wordlist_file = "wordlist.txt"
    brute_force_password(hash_to_crack, wordlist_file)
