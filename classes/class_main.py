from User import User
from UserAnnotation import UserAnnotation
from ClassMethod import ClassMethod

user = User("ajay")
user_annotation = UserAnnotation("ajay")
print(user.get_name())
user.set_name("raj")

print(user.private_name)
# Since property() is set via name. we can use name instead of private_name
user.name = "jaga"
print(user.name)
print("User annotation:")
print(user_annotation.private_name)
print(user_annotation.name)
user_annotation.name = "jaga"
print(user_annotation.name)

ClassMethod.printLog()

cm = ClassMethod()
cm_a = ClassMethod()
cm_b = ClassMethod()
cm.print()
cm.normal()
ClassMethod.printLog()