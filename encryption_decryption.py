def encrypt_text(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char

        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char

        else:
            encrypted_text += char 

    return encrypted_text

text = input("Enter the text to encrypt: ")

shift = int(input("Enter the shift value: "))

encrypted_text = ""

for char in text:
    if char.isalpha():
        if char.islower():
            base = ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)

        else:
            base = ord('A')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
    else:
        encrypted_text += char
print("Encrypted text: ", encrypted_text)

decrypted_text = ""

for char in encrypted_text:
    if char.isalpha():
       if char.islower():
           base = ord('a')
           decrypted_text += chr((ord(char) - base - shift) % 26 + base)
       else:
           base = ord('A')
           decrypted_text += chr((ord(char) - base - shift) % 26 + base)
    else:
        decrypted_text += char
print("Decrypted text:" , decrypted_text)
           


     

