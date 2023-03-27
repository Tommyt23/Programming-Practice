# Using tutorial: https://www.futurelearn.com/courses/object-oriented-principles/21/todo
from room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining = Room("Dining Room")

kitchen.set_description("A dank and dirty room buzzing with flies.")

print(kitchen.get_description())
kitchen.describe()

kitchen.set_name("cooking room")
print(kitchen.get_name())
kitchen.named()