# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter a non-negative number: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i

    print("Factorial is:", factorial) #using for loop


#Solution - 2
# number = int(input("Enter a non-negative number: "))
# factorial = 1
# while number>0:
#     factorial=factorial*number
#     number=number-1
    
# print("Factorial",factorial) #using While Loop
