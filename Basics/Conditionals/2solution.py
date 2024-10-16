#movie ticket -> 12 dollars for adults (18 and over)
# 8 dollars for children (less than 18)
# everyone gets a 2 dollar on wednesday

age=int(input("Enter your age"))
day=str(input("Enter day"))

# price=12 if age>=18 else 8

if age>=18:
    price=12
else:
    price=8

if day=="wed":
    price-=2
    
print("Ticket price for you is $",price)


#Solution-2
# age=int(input("Enter your age"))
# day=str(input("Enter day"))

# if age>=18:
#     print("12 dollars ")
# elif age<18:
#     print("children ")
# if(day=="wed"):
#     print("Additional 2 dollar discount")