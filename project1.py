# Password Strength Checker

password = input("Enter your password: ")

length = len(password)

has_upper = False
has_digit = False
has_symbol = False

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True

score = 0

# Check password length
if length >= 8:
    score += 1

# Check uppercase letter
if has_upper:
    score += 1

# Check digit
if has_digit:
    score += 1

# Check special symbol
if has_symbol:
    score += 1

# Display result
print("\n========== Password Analysis ==========")
print("Password Score :", score, "/4")

if score <= 1:
    print("Password Strength : Weak")
elif score <= 3:
    print("Password Strength : Medium")
else:
    print("Password Strength : Strong")

# Suggestions
print("\nSuggestions:")

if length < 8:
    print("- Make the password at least 8 characters long.")

if not has_upper:
    print("- Add at least one uppercase letter.")

if not has_digit:
    print("- Add at least one number.")

if not has_symbol:
    print("- Add at least one special character (@, #, $, etc.).")

if score == 4:
    print("- Excellent! Your password is strong.")

print("======================================")