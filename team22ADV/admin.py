from django.contrib import admin
from .models import Room, Player

# Register your models here.
admin.site.register(Room) # register the Room model with the admin site 
admin.site.register(Player) # register the Player model with the admin site 
