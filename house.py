import pyblockworld

from wall import Wall
from roof import Roof


class House:

    # Aggregation:
    # hat-Beziehung, besitzt-Beziehung
    # „ist Teil von“, „besteht aus“, „hat“

    # Komposition:
    # Die Komposition ist eine Sonderform der Aggregation.
    # Sie drückt aus, dass die Teile von der Existenz des Ganzen abhängig sind.

    def __init__(self, wallFront: Wall, wallLeft: Wall, wallRight: Wall, wallBack: Wall, pos: tuple, roof: Roof, bw: pyblockworld.World):
        self.wallFront: Wall = wallFront
        self.wallLeft: Wall = wallLeft
        self.wallRight: Wall = wallRight
        self.wallBack: Wall = wallBack
        self.pos: () = pos
        self.roof: Roof = roof
        self.__bw: pyblockworld.World = bw

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
