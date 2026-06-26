"""
Sequential Pattern Detection
"""

SEQUENCES = [
    "123456",
    "abcdef",
    "qwerty",
    "987654"
]

def contains_sequence(password):

    password = password.lower()

    for sequence in SEQUENCES:

        if sequence in password:

            return True

    return False
