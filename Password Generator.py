import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    
    if include_digits:
        characters += string.digits
    
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
s    return password


while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Please enter a positive password length.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


password = generate_password(length=password_length, include_digits=True, include_special_chars=True)
print("Generated Password:", password)
