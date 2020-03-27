# Strings are immutable. None of the changes affect the original variable unless assigned
import string

extractor="Hello World"
print("Full String: ", extractor[:])

print("Offset from 3: ", extractor[3:])
print("Offset from :3 ", extractor[:3])
print("Offset from 3:8 ", extractor[3:8])

print("Last 3 characters: ", extractor[-3:])
print("Last 3 characters: ", extractor[4:-3])

print("By space: ", extractor.split(" "))

strip_variable = "This has punctuations ..!!"
print("Strip Punctuations: ", strip_variable.strip(string.punctuation))
print("Strip White spaces: ", strip_variable.strip(string.whitespace))
print("Strip Punctuations and White spaces: ", strip_variable.strip(string.whitespace + string.punctuation))

print("Find the: ", strip_variable.find("the")) 
print("rFind the: ", strip_variable.rfind("the")) 
print("Find has: ", strip_variable.find("has")) 

# Returns substring not found error unlike -1 in find
# print("Index the: ", strip_variable.index("the"))
# print("rIndex the: ", strip_variable.rindex("the"))


count_variable = "This has repeated texts for counting texts"
print("Count: ", count_variable.count("text"))

alpha_variable = "Thishasnumbersandtexts2"
print("alpha_variable isAlphanumberic: ", alpha_variable.isalnum())
print("count_variable isAlphanumberic: ", count_variable.isalnum())

title = "This is a title"
print("Title: ", title.title())
