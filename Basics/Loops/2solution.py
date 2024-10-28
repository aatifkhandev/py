# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)



#Solution - 2
# n=10
# sum_even=0
# for i in range(0,n+1):
#     print(i)
#     if i%2==0:
#         sum_even+=i
        
# print(sum_even) 