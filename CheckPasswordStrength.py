import re
def check_password_strength(password):
    strength_score = 0
    if len(password) >= 8:
        strength_score += 1
    else:
        return "Weak password!"
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength_score += 1
    if re.search(r'[0-9]', password):
        strength_score += 1
    if re.search(r'[@#$%^&+=!]', password):
        strength_score += 1
    if not re.search(r'(1234|abcd|qwerty|password|admin|letmein)', password, re.IGNORECASE):
        strength_score += 1
    else:
        return "Weak password!."
    if strength_score == 5:
        return "Strong password!"
    elif strength_score == 4:
        return "Medium strength password."
    elif strength_score <= 3:
        return "Weak password!"
    else:
        return "Invalid password."
password = input("Enter your password: ")
print(f"Password: {password} => Strength: {check_password_strength(password)}")

