import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True, use_uppercase=True, use_lowercase=True):
    characters = ''
    if use_special_chars:
        characters += string.punctuation
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("At least one character set must be enabled")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Enter password length: "))
    use_special_chars = input("Use special characters? (yes/no): ").lower() == 'yes'
    use_digits = input("Use digits? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_special_chars, use_digits, use_uppercase, use_lowercase)
    print(f"Generated Password: {password}")
