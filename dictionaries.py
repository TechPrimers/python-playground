# Order doesn't matter like HashMap
dictionary = {"name": "ajay", "location": "chennai"}

for item in dictionary:
    print(f"key[{item}] value [{dictionary[item]}]in dictionary")
    print(f"Another representation: key[{item}] value [{dictionary.get(item)}]in dictionary")

print("Only keys: ", dictionary.keys())

dictionary_keys = list(dictionary.keys())
print("Keys: ", dictionary_keys)
print("Keys (type): ", type(dictionary_keys))


dictionary_values = list(dictionary.values())
print("Values: ", dictionary_values)
print("Values (type): ", type(dictionary_values))


dictionary_list_items = list(dictionary.items())
print("Items: ", dictionary_list_items)
print("Items (type): ", type(dictionary_list_items))