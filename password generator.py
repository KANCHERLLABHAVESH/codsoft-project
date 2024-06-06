import string
import random

def generate_password(length):
    if length < 4:  # Ensure password length is sufficient for complexity
        return "Password length should be at least 4 characters."

    # Define the character sets to include in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

def main():
    try:
        # Get user input for the password length
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
