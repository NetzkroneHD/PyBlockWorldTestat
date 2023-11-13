import unittest
import pyblockworld

from house import House
from roof import Roof
from wall import Wall


class HouseTest(unittest.TestCase):

    def setUp(self):
        self.world: pyblockworld.World = pyblockworld.World()

        self.wallFront: Wall = Wall(pos=(1, 1, 1), material_id="", bw=self.world)
        self.wallLeft: Wall = Wall(pos=(2, 2, 2), material_id="", bw=self.world)
        self.wallRight: Wall = Wall(pos=(3, 3, 3), material_id="", bw=self.world)
        self.wallBack: Wall = Wall(pos=(4, 4, 4), material_id="", bw=self.world)
        self.pos: tuple = (0, 0, 0)
        self.roof: Roof = Roof(pos=(5, 5, 5), bw=self.world)
        self.house = House(wallFront=self.wallFront, wallLeft=self.wallLeft, wallRight=self.wallRight, wallBack=self.wallBack, pos=(5, 5, 5),
                      roof=self.roof,
                      bw=self.world)
        pass

    def test_change_wall_material(self):
        new_mat = "new_mat"
        self.house.change_wall_material(new_mat)
        self.assertEquals(new_mat, self.wallFront.material_id)
        self.assertEquals(new_mat, self.wallLeft.material_id)
        self.assertEquals(new_mat, self.wallRight.material_id)
        self.assertEquals(new_mat, self.wallBack.material_id)


unittest.main()
