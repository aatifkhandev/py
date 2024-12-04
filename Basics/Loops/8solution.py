# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)














# def isPrime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True  

# number = int(input("Enter a Number: "))
# if isPrime(number):
#     print("The Number is Prime")
# else:
#     print("Not a Prime Number")
