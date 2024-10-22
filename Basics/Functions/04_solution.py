# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.


import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)


#Solution - 2
# def Circle(radius):
#     area=2*3.14*radius
#     circumference=2*3.14*radius
#     return area,circumference

# print(Circle(2))