from pyblockworld import World

from house import House
from roof import Roof
from wall import Wall
from wall_with_door import WallWithDoor
from wall_with_window import WallWithWindow

type = int(input("Testat Aufgabe: "))


#
# BEISPIEL 1
#

# Eine Funktion, die beim Drücken der B-Taste aufgerufen werden soll
def b_key_pressed(world: World):
    if type == 2:
        wall_rotated = Wall(pos=world.player_position(), bw=world, rotated=True)
        wall = Wall(pos=world.player_position(), bw=world)
        wall_rotated.build()
        wall.build()
    elif type == 3:
        wall_rotated = WallWithDoor(pos=world.player_position(), bw=world, rotated=True)
        wall = WallWithDoor(pos=world.player_position(), bw=world)
        wall_rotated.build()
        wall.build()
    elif type == 4:
        wall_rotated = WallWithWindow(pos=world.player_position(), bw=world, rotated=True)
        wall = WallWithWindow(pos=world.player_position(), bw=world)
        wall_rotated.build()
        wall.build()
    elif type == 5:
        wall_rotated = Roof(pos=world.player_position(), bw=world)
        wall_rotated.build()
    elif type == 6:
        house = House(world.player_position(), world)
        house.build()


# Erstellen einer neuen Welt
world = World()
# Die Funktion für die build-Taste (b) wird zugewiesen
world.build_key_pressed = b_key_pressed
# Die Welt wird gestartet
world.run()

