# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

weather=str(input("Enter Weather"))

if weather=="sunny":
    activity="Go for a Walk"
elif weather=="rainy":
    activity="Read a book"
elif weather=="snowy":
    activity="Build a snow"
    
print("Activity to do in this weather is",activity)