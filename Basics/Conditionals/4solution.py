# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit=str(input("Enter a fruit"))
state=str(input("Enter it's state"))

if fruit=="Green":
    print("unripe")
elif fruit=="yellow":
    print("ripe")
elif fruit=="Brown":
    print("overripe")