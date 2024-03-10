import random
import string

def generator(uppercase: bool, lowercase: bool, numbers: bool, symbols: bool, length: int) -> None:
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        print("You're password should at least contains any one of the above!")
        return None
    
    password = "".join(random.choice(characters) for _ in range(length))

    return password

print("Type Yes/yes to include or anything else to not include in the password.")
uppercase = input("Do you want any uppercase letters: ").lower() == "yes"
lowercase = input("Do you want any lowercase letters: ").lower() == "yes"
numbers = input("Do you want any numbers: ").lower() == "yes"
symbols = input("Do you want any symbols: ").lower() == "yes"

length = int(input("Enter the length you're password should have (6 - 16):"))

password = generator(uppercase, lowercase, numbers, symbols, length)
if password:
    print(f"You're password is \" {password} \"")