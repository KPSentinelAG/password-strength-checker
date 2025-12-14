# Password Strength Checker
This project is a password strength checker written in Python.

## Objectives
- First Objective: Build an automated tool that rates a user's password strength (Weak, Medium, Strong).
- Second Objective: If a user's password is rated 'Weak' or 'Medium', the tool provides suggestions to improve it.
- Third Objective: Check a user's password against a list of the top 1,000 commonly used passwords.

This basic security automation tool demonstrates the concepts of input validation, error handling, and file handling.  

## Features
1. Check for minimum password length requirement (12+ characters)
2. Check for the presence of a lowercase character.
3. Check for the presence of an uppercase character.
4. Check for the presence of a number.
5. Check for the presence of a special character.
6. Check for 3 consecutive descending or ascending characters.
7. Check the password against the top 1,000 commonly used passwords.
8. Rate the user's password as: Weak, Medium, or Strong.
9. Suggest improvements to the password if it is rated as Weak or Medium.

## Dependencies
This is meant to run as a standalone tool, so no additional libraries or software are needed.

## Prerequisites
- Python version 3 is needed
- Download 'password_checker.py' script 
- Download 'common_passwords.txt'
- Place both files in the same folder.  

## Additional Information
- Any passwords that are found in the common_passwords.txt list are automatically rejected, even if they meet other strength requirements.
- The top 1,000 common passwords list was sourced from the SecLists GitHub repository.
