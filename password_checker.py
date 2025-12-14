#-------------------------------------CHECKING FUNCTIONS---------------------------------------------
# Function to check for password length
def length_check(password):
    # Return true if length is 12 or greater
    return len(password) >= 12

# Function to check for uppercase letter
def uppercase_check(password):
    # Iterate through each character in the password and check for uppercase letter
    for char in password:
        if char.isupper():
             return True
        
    return False

# Function to check for lowercase letter
def lowercase_check(password):
    # Iterate through each character in the password and check for lowercase letter
    for char in password:
        if char.islower():
            return True
    
    return False

# Function to check for numbers
def number_check(password):
    # Iterate through each character in the password and check for numbers
    for char in password:
        if char.isdigit():
            return True
    
    return False

# Function to check for characters
def special_character_check(password):
    # Set a list of special characters
    special = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "/", "?", "\\", ".", "<", ">", ":", ";"]

    # Iterate through each character in the password and see if it matches with any character in the special list
    for char in password:
        if char in special:
            return True
    
    return False

# Function to check for consecutives
def consecutive_check(password):
    # Convert the password to lowercase for easier comparison
    password_lowercase = password.lower()

    # Iterate through the password to check groups of three characters
    for i in range(len(password_lowercase) - 2):
        char1 = password_lowercase[i]
        char2 = password_lowercase[i + 1]
        char3 = password_lowercase[i + 2]

        # Check if all three characters are letters
        if char1.isalpha() and char2.isalpha() and char3.isalpha():
            char1_ascii = ord(char1)
            char2_ascii = ord(char2)
            char3_ascii = ord(char3)

            # Check to see if they are consecutive letters in ascending order
            if char2_ascii == char1_ascii + 1 and char3_ascii == char2_ascii + 1:
                return True
            
            # Check to see if they are consecutive letters in descending order
            if char3_ascii == char2_ascii - 1 and char2_ascii == char1_ascii - 1:
                return True
        
        # Check if all three characters are numbers
        elif char1.isdigit() and char2.isdigit() and char3.isdigit():
            num1_ascii = ord(char1)
            num2_ascii = ord(char2)     
            num3_ascii = ord(char3)

            # Check if the numbers are consecutive in ascending order
            if num2_ascii == num1_ascii + 1 and num3_ascii == num2_ascii + 1:
                return True
            
            # Check if the numbers are consecutive in descending order
            if num3_ascii == num2_ascii - 1 and num2_ascii == num1_ascii - 1:
                return True
        
    return False

def common_password_check(password):
    user_password = password.lower()

    with open("common_passwords.txt", "r") as file:
        for line in file:
            file_password = line.lower().strip()

            if file_password == user_password:
                return True
        
        return False

#-------------------------------------STRENGTH CHECKING FUNCTION-------------------------------------
# Check the result of each function and keep track of the total score
def strength_check(length_result, uppercase_result, lowercase_result, number_result, special_char_result, consecutive_result):
    # Create a variable to keep track of the score
    strength_score = 0

    # The functions below add one point to the total score if the requirement is met
    if length_result is True:
        strength_score += 1
    
    if uppercase_result is True:
        strength_score += 1

    if lowercase_result is True:
        strength_score += 1
    
    if number_result is True:
        strength_score += 1
    
    if special_char_result is True:
        strength_score += 1
    
    if consecutive_result is False:
        strength_score += 1

    # Rate the password based on the number of points
    if strength_score == 6:
        return "Strong"
    elif strength_score == 4 or strength_score == 5:
        return "Medium"
    else:
        return "Weak"

#-------------------------------------IMPROVEMENTS FUNCTION---------------------------------------
# Function to suggest improvements for the user's password
def improvement_suggestions(length_result, uppercase_result, lowercase_result, number_result, special_char_result, consecutive_result):
    # Create a list to contain the suggestion messages
    suggestions = []

    # Add the suggestions into the suggestion list if the conditions is not met
    if length_result is False:
        suggestions.append("You need 12 or more characters.")

    if uppercase_result is False:
        suggestions.append("You need at least 1 uppercase character.")
    
    if lowercase_result is False:
        suggestions.append("You need at least 1 lowercase character.")

    if number_result is False:
        suggestions.append("You need at least 1 number.")
    
    if special_char_result is False:
        suggestions.append("You need at least 1 special character.")
    
    if consecutive_result is True:
        suggestions.append("You should not have 3 consecutive numbers or characters.")
    
    # Return the list of suggestions
    return suggestions

#-------------------------------------MAIN--------------------------------------------------------
print("WELCOME TO THE PASSWORD STRENGTH CHECKER!")

# Ask the user to enter a password. 
while True:
    user_pass = input("Enter a password to check its strength: ")

    # Remove leading and trailing whitespaces.
    # If user password is blank or contain only white spaces, tell the user to re-enter 
    if user_pass.strip() == "":
        print("Your password should not be empty or contain only spaces.")
        continue
    
    # If user password is in the list of common passwords, tell the user to re-enter
    common_result = common_password_check(user_pass)
    if common_result is True:
        print("This password is on the commonly used list of passwords. Please choose another password.")
        continue
    
    break

# Check password requirements using each function
length_result = length_check(user_pass)
uppercase_result = uppercase_check(user_pass)
lowercase_result = lowercase_check(user_pass)
number_result = number_check(user_pass)
special_char_result = special_character_check(user_pass)
consecutive_result = consecutive_check(user_pass)

# Generate the password strength
password_strength = strength_check(length_result, uppercase_result, lowercase_result, number_result, special_char_result, consecutive_result)

# Let the user know their password score
print("Your password strenth is:", password_strength)

# If password is Medium or Weak, generate a list of improvement suggestions. 
if password_strength == "Medium" or password_strength == "Weak":
    suggestions = improvement_suggestions(length_result, uppercase_result, lowercase_result, number_result, special_char_result, consecutive_result)
    print("YOUR PASSWORD IS", password_strength.upper(), "HERE IS A LIST OF IMPROVEMENTS YOU SHOULD MAKE:")
    for suggestion in suggestions:
        print(suggestion)