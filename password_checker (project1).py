password = input("Enter your password: ")
print(password)
length = len(password)
print(length)
if length < 8:
    print("Weak Password")
if length >= 8:
    if "@" in password:
         print("Good Password")
has_number = any(char.isdigit() for char in password)
if has_number:
        print("Password contains a number")
has_upper = any(char.isupper() for char in password)
if has_upper:
    print("Password contains an uppercase letter")
has_lower = any(char.islower() for char in password)
if has_lower:
    print("Password contains an lowercase letter")
special_charcters = "!@#$%^&*"
has_special = any(char in special_charcters for char in password)
if has_special:
     print("Password contains a special character")
if length >= 8 and has_upper and has_lower and has_upper and has_number and has_special:
     print("Strong password")
else:
     print("Weak password")