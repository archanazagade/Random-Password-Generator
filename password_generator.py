import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters  # a-zA-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # Special characters

    if not characters:
        print("⚠️ You must select at least one character type.")
        return None

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Random Password Generator!\n")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("⚠️ Length must be a positive number.")
            return

        # Character type preferences
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_digits, use_symbols)
        if password:
            print(f"\n✅ Your generated password is: {password}")

    except ValueError:
        print("⚠️ Please enter a valid number for length.")

if __name__ == "__main__":
    main()
