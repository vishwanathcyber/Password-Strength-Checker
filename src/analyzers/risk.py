"""
Password Risk Classification
"""

def classify(score):

    if score >= 90:
        return "Very Strong"

    elif score >= 70:
        return "Strong"

    elif score >= 50:
        return "Moderate"

    else:
        return "Weak"
