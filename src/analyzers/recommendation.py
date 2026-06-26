"""
Password Recommendations
"""

def generate_recommendations(password):

    recommendations = []

    if len(password) < 12:
        recommendations.append("Increase password length.")

    if not any(c.isupper() for c in password):
        recommendations.append("Add uppercase letters.")

    if not any(c.islower() for c in password):
        recommendations.append("Add lowercase letters.")

    if not any(c.isdigit() for c in password):
        recommendations.append("Add numbers.")

    if not any(not c.isalnum() for c in password):
        recommendations.append("Add special characters.")

    return recommendations
