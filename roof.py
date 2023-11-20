import math

import pyblockworld


class Roof:
    def __init__(self, pos: tuple, bw: pyblockworld.World, roof_material_id: str = "default:brick", width=6, depth=6):
        self.width = width
        self.depth = depth
        self.pos = pos
        self.material_id = roof_material_id
        self.roof_material_id = roof_material_id
        self.__bw: pyblockworld.World = bw

    def build(self):
        x, y, z = self.pos
        x += 1
        steps = 0
        half = self.width // 2
        while steps <= half:
            self.__bw.setBlocks(math.ceil(x + steps), math.ceil(y), math.ceil(z),
                                math.ceil(x + self.width - steps), math.ceil(y + steps), math.ceil(z + self.depth),
                                self.roof_material_id)
            steps += 1
