import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
        
    
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please include at least one character type (letters, numbers, symbols)")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")
    
    
    while True:
        length_str = input("Enter the length of the password (at least 4 characters): ")
        if length_str.isdigit() and int(length_str) >= 4:
            length = int(length_str)
            break
        else:
            print("Please enter a valid password length (at least 4 characters).")

    
    include_letters = input("Include letters (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols (y/n): ").lower() == 'y'
    
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
