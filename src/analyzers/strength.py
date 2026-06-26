"""
Password Strength Analyzer
"""

from validators.length import check_length
from validators.characters import check_characters

def analyze_password(password):

    print("\nPassword Analysis\n")

    check_length(password)

    check_characters(password)
