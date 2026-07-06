# System Security Audit Tool

score = 0

# Take user input
firewall = input("Is Firewall Enabled? (yes/no): ").lower()
antivirus = input("Is Antivirus Installed? (yes/no): ").lower()
updates = input("Is your Operating System Updated? (yes/no): ").lower()
password = input("Are you using a Strong Password? (yes/no): ").lower()
twofa = input("Is Two-Factor Authentication Enabled? (yes/no): ").lower()

# Calculate score
if firewall == "yes":
    score += 1

if antivirus == "yes":
    score += 1

if updates == "yes":
    score += 1

if password == "yes":
    score += 1

if twofa == "yes":
    score += 1

# Display Report
print("\n========== Security Audit Report ==========")

print("Firewall                 :", firewall.capitalize())
print("Antivirus                :", antivirus.capitalize())
print("OS Updated               :", updates.capitalize())
print("Strong Password          :", password.capitalize())
print("Two-Factor Authentication:", twofa.capitalize())

print("\nSecurity Score:", score, "/5")

# Risk Level
if score == 5:
    print("Risk Level: LOW")
elif score >= 3:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: HIGH")

# Recommendations
print("\nRecommendations:")

if firewall == "no":
    print("- Enable Firewall.")

if antivirus == "no":
    print("- Install an Antivirus.")

if updates == "no":
    print("- Update your Operating System.")

if password == "no":
    print("- Use a Strong Password.")

if twofa == "no":
    print("- Enable Two-Factor Authentication.")

if score == 5:
    print("- Excellent! Your system follows basic security practices.")

print("==========================================")
