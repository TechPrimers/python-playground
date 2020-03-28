tuple_variable = ()
print("Empty tuple: ", tuple_variable)

single_tuple = ("single",)
print("Single tuple: ", single_tuple)
print("Single tuple(type): ", type(single_tuple))


str_tuple = ("single") # Without comma, tuples become str
print("Not a tuple: ", str_tuple)
print("Not a tuple(type): ", type(str_tuple))


declar_tuple = ("one", "two", "three")
print("Declaring tuples: ", declar_tuple)

declar_tuple = "one", "two", "three" # Another way of declaring tuples
print("Declaring tuples: ", declar_tuple)

assign_tuple1, assign_tuple2, assign_tuple3 = ("one", "two", "three")
print("Assigned tuple1: ", assign_tuple1)
print("Assigned tuple2: ", assign_tuple2)
print("Assigned tuple3: ", assign_tuple3)

#Flip variables using tuples without using a temporary variable
assign_tuple1, assign_tuple2 = assign_tuple2, assign_tuple1
print("Swapped tuple1: ", assign_tuple1)
print("Swapped tuple2: ", assign_tuple2)

#List to tuple
list_tuple = tuple(["one", "two", "three"])
print("List tuple: ", list_tuple)
print("List tuple(type): ", type(list_tuple))

for tup in list_tuple:
    print("items: ", tup)

print("List: ", list("test"))