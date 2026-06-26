"""
Character Validator
"""

import re

def check_characters(password):

    checks = {

        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Numbers": bool(re.search(r"[0-9]", password)),
        "Special Characters": bool(re.search(r"[^A-Za-z0-9]", password))

    }

    for check, result in checks.items():

        print(f"{check}: {'Yes' if result else 'No'}")
