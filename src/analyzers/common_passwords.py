"""
Common Password Detection
"""

COMMON_PASSWORDS = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome",
    "password123"
]

def is_common_password(password):

    return password.lower() in COMMON_PASSWORDS
