"""
Password Strength Checker

Main application entry point.
"""

from analyzers.strength import analyze_password

def main():

    print("=" * 50)
    print("Password Strength Checker")
    print("=" * 50)

    password = input("Enter password: ")

    analyze_password(password)

if name == "main":
    main()
