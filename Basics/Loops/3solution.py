# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n=int(input("Enter a Number : "))

for i in range(1,11):
    if i==5:
        continue
    print(n*i)
    

 
#Solution-2  
# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x', i, '=', number * i)