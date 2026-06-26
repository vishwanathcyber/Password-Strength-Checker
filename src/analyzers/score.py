"""
Password Score
"""

def calculate_score(password):

    score = 0

    if len(password) >= 12:
        score += 30

    if any(c.isupper() for c in password):
        score += 20

    if any(c.islower() for c in password):
        score += 20

    if any(c.isdigit() for c in password):
        score += 15

    if any(not c.isalnum() for c in password):
        score += 15

    return score
