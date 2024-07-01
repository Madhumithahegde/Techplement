# Simple Password Generator
This script generates a random password based on user-specified criteria, such as the length of the password and whether to include uppercase letters, lowercase letters, digits, and special characters.

# Usage
When you run the script, you will be prompted to provide the following inputs:
1. Length of the Password: Enter an integer value specifying the length of the password.
2. Include Uppercase Letters: Type yes to include uppercase letters, or no to exclude them.
3. Include Lowercase Letters: Type yes to include lowercase letters, or no to exclude them.
4. Include Digits: Type yes to include digits, or no to exclude them.
5. Include Special Characters: Type yes to include special characters, or no to exclude them.

# Code Explanation
The script consists of two main parts: the generate_password function and the main function.

**generate_password(length, use_upper, use_lower, use_digits, use_special)**

1. Parameters:
   1. length: Integer value for the length of the password.
   2. use_upper: Boolean value to include uppercase letters.
   3. use_lower: Boolean value to include lowercase letters.
   4. use_digits: Boolean value to include digits.
   5. use_special: Boolean value to include special characters.

2. Functionality:
   1. Builds a character pool based on the parameters.
   2. Generates a random password by selecting random characters from the pool.

**main()**
Functionality:
 1. Prompts the user to enter the password length and whether to include each type of character.
 2. Calls the generate_password function with the user inputs.
 3. Prints the generated password.

**Entry Point**
1. The script includes the following entry point to ensure it runs correctly when executed directly:
> if __name__ == "__main__":
>    import random
>    main()
2. This block ensures that the main function is only called when the script is executed directly, not when it is imported as a module.

# Sample Output
> Enter the length of the password:
8
Include uppercase letters? (yes/no):
yes
Include lowercase letters? (yes/no):
yes
Include digits? (yes/no):
no
Include special characters? (yes/no):
yes
Generated password: :PKFDe=X

# Additional Info
1. The script uses the random module, which is part of the Python Standard Library.
2. The script does not handle invalid inputs (e.g., non-integer length or unexpected responses to yes/no questions) robustly. Ensure to enter valid inputs as prompted.
