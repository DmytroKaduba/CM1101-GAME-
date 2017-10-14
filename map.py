"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Room():
    def __init__(self, name, des, exits, items):
        self.name = name
        self.description = des
        self.exits = exits
        self.items = items

##########################################
#Create the rooms
none = Room('', '', '', '')
room_hall = Room('Hall', 'You enter a long hall with various portraits on the walls.', {'south' : 'Reception'}, ['notebook'] )
room_reception = Room('Reception', 'You enter the main reception of the building. The room is empty.', {'north': 'Hall'},[])

#room dictionary for navigation
rooms = {
    'Reception' : room_reception,
    'Hall' : room_hall


}
