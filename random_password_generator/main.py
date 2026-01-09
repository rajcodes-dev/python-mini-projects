# collect user preferences:
# - length
# - should contain uppercase
# - should contain digits
# - should contain special

# get all availabe characters
# randomly pick character up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string


def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters?(yes/no) ").strip().lower()
    include_digit = input("Include digits?(yes/no) ").strip().lower()
    include_special = input("Include special characters?(yes/no) ").strip().lower()

    if length < 4:
        print("Password length must be atleast 4 characters.")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digit = string.digits if include_digit == "yes" else ""
    all_characters = lower + uppercase + special + digit

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))

    if include_digit == "yes":
        required_characters.append(random.choice(digit))

    if include_special == "yes":
        required_characters.append(random.choice(special))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)
