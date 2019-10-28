from django.contrib.auth.models import User
from team22ADV.models import Player, Room
Room.objects.all().delete()
# f = open('util/room_names.txt', 'r')
# room_names_file = f.read().split("\n")
# f.close()
room_names_file = ['The Parallel Realm', 'The All Fields', 'Pits of the Elemental Mountain', 'Point of the MourningDragon', 'Delves of the Mad Guardian', 'Quarters of the Mythic Occult', 'The Phantom Caverns', 'The Lurking Shadow Tombs', 'The Lower Crypt', 'The Brilliant Tombs', 'The Phantom Labyrinth', 'The Bloodfall Dungeon', 'The False Haven', 'The Central Land', 'The Fire Rift', 'The Polished Universe', 'The Distant Shore', 'The Forgotten Shores', 'The Soothing World', 'The Counter Continent', 'The Marble Moon', 'The Moulded Haven', 'The Arrival Forest', 'The Infected Shore', 'The Roaring Acres', 'The Liberty Rift', 'The Mad Universe', 'The Edge Continent', 'Grotto of the Granite Forest', 'Delvesof the Raging Soldier', 'Point of the Crying Priest', 'Vault of the Mourning Elf', 'The Abominable Lair', 'The Orc Tombs', 'The Ghost Crypt', 'The Forgotten Maze', 'The Adamantite Delves', 'The Turbulent Pits', 'The Cleansed Planet', 'The Hidden Globe', 'The Liberty Lands', 'The Metal Havens', 'The Infinite Realm', 'The Harmony Shore', 'The Possessed Fields', 'The Vacant World', 'The Fairy Domain', 'The Resting Earth', 'The Bruised Terrain', 'The Cleansed Moon', 'The Golden Planet', 'The Perfected Realm', "The God's Globe", 'The Dual Domain', 'The Adamant Territory', 'The Crown Territories', 'The Twisted Continent', 'The Unmade Moon', 'The Dead Acres', 'The Eventide Forest', 'The Molten Realms', 'The Polished Realm', 'The Infantile World', 'The Electric Haven', 'The Metal Rift', 'The Half Terrain', 'The Faded Domain', 'The Enchanting Land', 'The End Territory', 'The Spirit Expanse', 'The Utopian Region', 'The Lonely Shores', 'Cells of the Renegade Legion', 'Pits of the Haunted Spider', 'Caverns of the Infernal Hunter', 'Chambers of the Thunder Wizard', 'The Specter Pits', 'The False Burrows', 'The Cursed Point', 'The Lion Tooth Delves', 'The Molten Pits', 'The Prisoner Haunt', 'The Nether Continent', 'The Upside-down Realm', 'The Darkness Planet', 'The Possessed Expanse', 'The Lone Universe', 'The Arid Shore', 'Tombs of the Forgotten Warrior', 'Point of the Crystal Serpent', 'Quarters of the Uncanny Basilisk', 'Cells of the Ebon Basilisk', 'The Terraced Lair', 'The Grey Delves', 'The Steel Point', 'The Lion Tooth Point', 'The Obliterated Catacombs', 'The Arching Dungeon', 'The Twin Realms', 'The Infected Havens']

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