"""
Length Validator
"""

def check_length(password):

    if len(password) >= 12:

        print("✓ Password length is strong.")

    elif len(password) >= 8:

        print("! Password length is acceptable.")

    else:

        print("✗ Password is too short.")
