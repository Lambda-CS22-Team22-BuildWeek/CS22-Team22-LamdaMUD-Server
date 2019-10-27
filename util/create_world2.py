from django.contrib.auth.models import User
from team22ADV.models import Player, Room
Room.objects.all().delete()
f = open('room_names.txt', 'r')
room_names_file = f.read().split("\n")
f.close()
room_names_dict = {}
room_objects_array = []
for name in room_names_file:
    room_names_dict[f"r_{name.lower().replace(' ', '_')}"] = Room(title=name, description=name)
for room in room_names_dict:
    room_objects_array.append(room_names_dict[room])
for i in range(len(room_objects_array)):
    room_objects_array[i].save()
going_up = True
for i in range(len(room_objects_array) - 1):
    if (i + 1) % 5 == 0 and i < len(room_objects_array) - 10:
        room_objects_array[i].connectRooms(room_objects_array[i + 10], "e")
        room_objects_array[i + 10].connectRooms(room_objects_array[i], "w")
    if (i + 1) % 10 == 0:
        going_up = not going_up
        room_objects_array[i].connectRooms(room_objects_array[i + 1], "e")
        room_objects_array[i + 1].connectRooms(room_objects_array[i], "w")
    elif going_up == True:
        room_objects_array[i].connectRooms(room_objects_array[i + 1], "n")
        room_objects_array[i + 1].connectRooms(room_objects_array[i], "s")
    elif going_up == False:
        room_objects_array[i].connectRooms(room_objects_array[i + 1], "s")
        room_objects_array[i + 1].connectRooms(room_objects_array[i], "n")
room_objects_array[len(room_objects_array) - 1].connectRooms(room_objects_array[0], "w")
room_objects_array[0].connectRooms(room_objects_array[len(room_objects_array) - 1], "e")
players=Player.objects.all()
for p in players:
  p.currentRoom=1
  p.save()