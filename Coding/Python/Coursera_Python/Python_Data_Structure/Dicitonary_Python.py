############ Dictionary in Python ############
# A dictionary in Python is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are mutable, which means that you can change the contents of a dictionary after it has been created. They are defined using curly braces {} and the key-value pairs are separated by commas. Here are some examples of how to create and use dictionaries in Python:
# Example 1: Creating a dictionary
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
print(my_dict)  # Output: {'name': 'Ayush', 'age': 25, 'city': 'New York'}
# Example 2: Accessing values in a dictionary
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Ayush
print(my_dict["age"])  # Output: 25
print(my_dict["city"])  # Output: New York
# Example 3: Modifying values in a dictionary
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
my_dict["age"] = 26  # This will change the value associated with the key "age" to 26
print(my_dict)  # Output: {'name': 'Ayush', 'age': 26, 'city': 'New York'}
# Example 4: Adding new key-value pairs to a dictionary
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
my_dict["country"] = "USA"  # This will add a new key-value pair to the dictionary with the key "country" and the value "USA"
print(my_dict)  # Output: {'name': 'Ayush', 'age': 25, 'city': 'New York', 'country': 'USA'}
# Example 5: Removing key-value pairs from a dictionary
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
del my_dict["age"]  # This will remove the key-value pair with the key "age" from the dictionary
print(my_dict)  # Output: {'name': 'Ayush', 'city': 'New York'}
my_dict.pop("city")  # This will remove the key-value pair with the key "city" from the dictionary and return the value associated with that key
print(my_dict)  # Output: {'name': 'Ayush'}
# Example 6: Dictionary methods
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
print(my_dict.keys())  # This will return a view object containing the keys of the dictionary
print(my_dict.values())  # This will return a view object containing the values of the dictionary
print(my_dict.items())  # This will return a view object containing the key value pairs of the dictionary as tuples 

################### for searching the key present in the dictionary or not ##############
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
print("name" in my_dict)  # This will return True because the key "name" is present in the dictionary
print("country" in my_dict)  # This will return False because the key "country" is not present in the dictionary    

##################### Get method in dictionary ##############
my_dict = {"name": "Ayush", "age": 25, "city": "New York"}
print(my_dict.get("name"))  # This will return the value associated with the key "name", which is "Ayush"
print(my_dict.get("country"))  # This will return None because the key "country" is not present in the dictionary. The get method returns None by default if the key is not found in the dictionary. You can also specify a default value to return if the key is not found by passing it as the second argument to the get method. For example:
print(my_dict.get("country", "Not Found"))  # This will return "Not Found" because the key "country" is not present in the dictionary, and we have specified "Not Found" as the default value to return if the key is not found.            