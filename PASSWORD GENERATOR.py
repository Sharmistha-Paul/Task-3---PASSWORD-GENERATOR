#PASSWORD GENERATOR
import random
import string

def generate_password(length):
    # Define character sets for password composition
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure a minimum length for the password
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))

        # Generate the password
        password = generate_password(length)

        if password:
            # Display the password
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()