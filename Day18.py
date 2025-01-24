import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    # Hash the input password and compare it to the stored hash
    return stored_hash == hash_password(password)

# Example usage
if __name__ == "__main__":
    known_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddf8e6f7c3a5e5e5e5e"  # Hash for "password"
    user_password = input("Enter your password: ")

    if verify_password(known_hash, user_password):
        print("Password is correct.")
    else:
        print("Password is incorrect.")