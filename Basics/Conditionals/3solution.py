# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


score=int(input("Enter your score"))

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)


#Solution-2
# score=int(input("Enter Your Score : "))

# if 90<=score<100:
#     print("A")
# elif 80<=score<89:
#     print("B")
# elif 70<=score<79:
#     print("C")
# elif 60<=score<69:
#     print("D")
# else:
#     print("F")
    
    
    
    
