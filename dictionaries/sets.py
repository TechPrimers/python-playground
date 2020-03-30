# Set has similar notation to dictionaries with {} however they have only keys
# elements in a set are unique compared to lists
sets = {"z","a", "b", "c"}
print("Type: ", type(sets))
print("Pop: ", sets.pop())
print("Sorted Set(list): ", sorted(sets))

list_var = ["a", "a", "z", "d", "c", "z"]
print("Sorted List: ", sorted(list_var))
print("Sorted in reverse: ", sorted(list_var, reverse = True))

print("Remove duplicates from list: ", sorted(list(set(list_var))))
