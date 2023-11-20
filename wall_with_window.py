import pyblockworld

from wall import Wall


class WallWithWindow(Wall):

    def __init__(self, pos: tuple, bw: pyblockworld.World, window_material_id: str = "air", rotated=False, width=6, height=5):
        super().__init__(pos, bw, rotated=rotated, width=width, height=height)
        self.window_material_id = window_material_id

    def build(self):
        super().build()
        x, y, z = self.pos
        x += 1
        window_width: int
        window_height: int
        if self.width >= 4:
            window_width = 2
        else:
            window_width = 1
        if self.height >= 4:
            window_height = 2
        else:
            window_height = 1
        window_start_pos = self.width / 2
        if self.rotated:
            print("rotated with window")
            self._bw.setBlocks(x, y, z + window_start_pos, x, y + window_height, z + window_width, self.window_material_id)
        else:
            print("with window")
            self._bw.setBlocks(x+window_start_pos, y, z, x+window_height, y + window_height, z, self.window_material_id)