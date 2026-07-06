# Basic Encryption & Decryption (Caesar Cipher)

text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

# Encryption
for char in text:
    if char.isalpha():
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted += char

decrypted = ""

# Decryption
for char in encrypted:
    if char.isalpha():
        if char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
    else:
        decrypted += char

print("\n========== Encryption Report ==========")
print("Original Message :", text)
print("Shift Key        :", shift)
print("Encrypted Text   :", encrypted)
print("Decrypted Text   :", decrypted)
print("=======================================")
