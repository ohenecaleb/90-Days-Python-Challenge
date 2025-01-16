# Program to validates email addresses using regular expressions.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


emails = ["test@example.com", "invalid-email@", "user.name@domain.co", "user@domain"]
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")