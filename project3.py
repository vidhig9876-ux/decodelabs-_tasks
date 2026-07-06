# Phishing Awareness Analyzer

message = input("Enter the email/message: ")

# Convert message to lowercase
message = message.lower()

# List of phishing keywords
phishing_keywords = [
    "click",
    "verify",
    "urgent",
    "password",
    "otp",
    "login",
    "bank",
    "account",
    "suspended",
    "immediately"
]

# Store detected red flags
red_flags = []

# Check for phishing keywords
for keyword in phishing_keywords:
    if keyword in message:
        red_flags.append(keyword)

count = len(red_flags)

# Display Report
print("\n========== Phishing Analysis ==========")
print("Total Red Flags Found:", count)

if count > 0:
    print("\nRed Flags:")
    for flag in red_flags:
        print("-", flag)

# Final Result
if count == 0:
    print("\nResult: Safe Message")
    print("Reason: No phishing keywords were detected.")

elif count <= 3:
    print("\nResult: Suspicious Message")
    print("Reason: The message contains some phishing indicators. Be careful before clicking any links.")

else:
    print("\nResult: Highly Suspicious Message")
    print("Reason: The message contains multiple phishing indicators. Do not trust it.")

print("=======================================")
