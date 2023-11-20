import pyblockworld

from wall import Wall


class WallWithDoor(Wall):

    def __init__(self, pos: tuple, bw: pyblockworld.World, door_material_id: str = "air", rotated=False, width=6, height=5):
        super().__init__(pos, bw, rotated=rotated, width=width, height=height)
        self.door_material_id = door_material_id

    def build(self):
        super().build()
        x, y, z = self.pos
        x += 1
        door_position = self.width / 2
        if self.rotated:
            print("rotated with door")
            self._bw.setBlocks(x, y-1, z + door_position, x, y+1, z + door_position, self.door_material_id)
        else:
            print("with door")
            self._bw.setBlocks(x+door_position, y-1, z, x + door_position, y +1, z, self.door_material_id)

