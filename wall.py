import pyblockworld


class Wall:
    def __init__(self, pos: tuple, bw: pyblockworld.World, material_id: str = "default:stone", rotated=False, width=6,
                 height=5):
        self.width: int = width
        self.height: int = height
        self.pos: () = pos
        self.rotated: bool = rotated
        self.material_id: str = material_id
        # Raute bedeutet protected also nur 1x _
        self._bw: pyblockworld.World = bw

    def build(self):
        x, y, z = self.pos
        x += 1
        if self.rotated:
            self._bw.setBlocks(x, -1, z, x, y + self.height, z + self.width, self.material_id)
        else:
            self._bw.setBlocks(x, -1, z, x + self.width, y + self.height, z, self.material_id)

    def set_block(self, bw):
        self._bw = bw

    def get_bw(self):
        return self._bw

    block_world = property(fget=get_bw, fset=set_block)
