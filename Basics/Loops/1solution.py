# 1. Counting Positive Numbers

# Problem: Given a list of numbers, count how many are positive.

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]



numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10,77]

positive_num_count=0

for i in numbers:
    if i>0:
        positive_num_count+=1
print("The final count is",positive_num_count)



# Solution - 2

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# count=0
# n=10

# for i in range(0,n):

#     if numbers[i]>0:

#         count+=1

# print("The Final Count is",count)
    