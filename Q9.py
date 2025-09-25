s = input("Enter a string: ")
n = int(input("Enter the shift value: "))

encrypted = ""
for char in s:
    if char.isalpha():
        if char.isupper():
            encrypted += chr((ord(char) - 65 + n) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + n) % 26 + 97)
    else:
        encrypted += char

print("Encrypted string:", encrypted)