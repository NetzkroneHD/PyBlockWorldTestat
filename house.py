import pyblockworld

from roof import Roof
from wall import Wall
from wall_with_door import WallWithDoor
from wall_with_window import WallWithWindow


class House:

    # Aggregation:
    # hat-Beziehung, besitzt-Beziehung
    # „ist Teil von“, „besteht aus“, „hat“

    # Komposition:
    # Die Komposition ist eine Sonderform der Aggregation.
    # Sie drückt aus, dass die Teile von der Existenz des Ganzen abhängig sind.

    def __init__(self, pos: tuple, bw: pyblockworld.World):
        self.pos = pos
        self.__bw = bw
        self.wallFront = WallWithDoor(bw=self.__bw, pos=self.pos)
        self.wallLeft = WallWithWindow(bw=self.__bw, pos=self.pos, rotated=True)
        x, y, z = self.pos
        right_wall_position = x + self.wallFront.width, y, z
        self.wallRight = WallWithWindow(bw=self.__bw, pos=right_wall_position, rotated=True)
        back_wall_position = x, y, z + self.wallRight.width
        self.wallBack = Wall(bw=self.__bw, pos=back_wall_position)
        y += self.wallLeft.height
        roof_pos = x, y, z
        self.roof = Roof(bw=self.__bw, pos=roof_pos)

    def build(self):
        self.wallFront.build()
        self.wallBack.build()
        self.wallLeft.build()
        self.wallRight.build()
        self.roof.build()

    def change_wall_material(self, new_material_id: str):
        self.wallFront.material_id = new_material_id
        self.wallLeft.material_id = new_material_id
        self.wallRight.material_id = new_material_id
        self.wallBack.material_id = new_material_id
