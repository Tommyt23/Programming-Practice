# Using tutorial: https://www.futurelearn.com/courses/object-oriented-principles/21/todo
class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)

    def set_name(self, roomName):
        self.name = roomName

    def get_name(self):
        return self.name
    
    def named(self):
        print(self.name)

    
