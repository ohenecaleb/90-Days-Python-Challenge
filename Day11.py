# Program to validates email addresses using regular expressions.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


emails = ["test@example.com", "invalid-email@", "user.name@domain.co", "user@domain"]
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")

#Explanation line 6 below
"""
[a-zA-Z0-9-]: This part of the pattern defines a character class that matches any single character that is:

A lowercase letter (a-z)
An uppercase letter (A-Z)
A digit (0-9)
A hyphen (-)
+: This quantifier means "one or more" of the preceding character class. 
It ensures that the pattern matches one or more characters from the character 
class [a-zA-Z0-9-].

\.: This matches a literal dot (.). The backslash (\) is used to escape the 
dot because, in regular expressions, a dot normally matches any character.
 Escaping it with a backslash makes it match only a literal dot.

 Code By Ohene Caleb
"""
