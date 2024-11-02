# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.


input_str="teeter"

# Step 1: Create a dictionary to store character counts
char_count={}

# Step 2: Count the occurrences of each character
for char in input_str:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

# Step 3: Find the first non-repeated character
for char in input_str:
    if char_count[char]==1:
        print(char)
        break



#Solution-2 
# input_str="teeteracacad"

# for char in input_str:
#     if input_str.count(char)==1:
#         print("First Non Repeated Character is",char)
#         break