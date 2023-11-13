from pyblockworld import World

from house import House
from roof import Roof
from wall import Wall
from wall_with_door import WallWithDoor
from wall_with_window import WallWithWindow


#
# BEISPIEL 1
#

# Eine Funktion, die beim Drücken der B-Taste aufgerufen werden soll
def b_key_pressed(world: World):
    wall = Wall(bw=world, pos=world.player_position())
    wall.build()

    rotated = Wall(bw=world, pos=world.player_position(), rotated=True)
    rotated.build()

    roof = Roof(bw=world, pos=world.player_position())
    roof.build()

    wall_with_window = WallWithWindow(bw=world, pos=world.player_position())
    wall_with_window.build()

    wall_with_window_rotated = WallWithWindow(bw=world, pos=world.player_position(), rotated=True)
    wall_with_window_rotated.build()

# Erstellen einer neuen Welt
world = World()
# Die Funktion für die build-Taste (b) wird zugewiesen
world.build_key_pressed = b_key_pressed
# Die Welt wird gestartet
world.run()

world = World()
world.build_key_pressed = b_key_pressed
world.run()
