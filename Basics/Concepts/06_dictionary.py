# Create a dictionary
my_dict = {
    "name": "abc",
    "age": 0,
    "country": "India"
}


# Accessing dictionary elements
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("country:", my_dict["country"])


# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
print("Occupation:", my_dict["occupation"])


# Modifying an existing key-value pair
my_dict["age"] = 1
print("Updated Age:", my_dict["age"])


# Removing a key-value pair
del my_dict["country"]
print("Updated Dictionary (After removing 'city' key):", my_dict)


# Checking if a key exists
if "name" in my_dict:
    print("'name' key exists in the dictionary")


# Iterating over dictionary keys and values
print("Iterating over keys and values:")
for key, value in my_dict.items():
    print(key, ":", value)



# Clearing the dictionary
my_dict.clear()
print("Cleared Dictionary:", my_dict)


my_dict = {x: x**2 for x in range(1, 6)}
print(my_dict)

my_dict = {x: x**3 for x in range(1, 11) if x % 2 == 0}
print(my_dict)
