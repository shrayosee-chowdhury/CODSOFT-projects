# PASSWORD GENERATOR

# A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to
# specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.



import random


upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "@#$&*"


def generate_password(length):
    all_characters = upper_case + lower_case + numbers + symbols
    password = ''.join(random.sample(all_characters, length))
    return password

def Password():
    try:
        
        length = int(input("Enter the desired password length: "))
        if length < 5:
            print("Password length should be at least 5 for better security.")
            return
        
        password = generate_password(length)
        
        
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

Password()
