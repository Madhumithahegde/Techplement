#generating random passwords with customizable length and complexity
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    charr = ''
    if use_upper:
        charr += upper
    if use_lower:
        charr += lower
    if use_digits:
        charr += digits
    if use_special:
        charr += special

    if not charr:
        raise ValueError("At least one character type must be selected")

    password = ''
    for _ in range(length):
        password += charr[random.randint(0, len(charr) - 1)]

    return password

def main():
    print("Enter the length of the password:")
    length = int(input())

    print("Include uppercase letters? (yes/no):")
    use_upper = input().lower() == 'yes'

    print("Include lowercase letters? (yes/no):")
    use_lower = input().lower() == 'yes'

    print("Include digits? (yes/no):")
    use_digits = input().lower() == 'yes'

    print("Include special characters? (yes/no):")
    use_special = input().lower() == 'yes'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    import random
    main()
