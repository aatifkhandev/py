# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)


#Solution - 2
# char=int(input("Enter the number of characters :" ))

# if char<6:
#     password="weak"
# elif char<=10:
#     password="medium"
# else:
#     password="Strong"
    
# print(password)