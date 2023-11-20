import unittest

import pyblockworld

from house import House


class HouseTest(unittest.TestCase):

    def setUp(self):
        self.world: pyblockworld.World = pyblockworld.World()
        self.house = House(pos=(5, 5, 5), bw=self.world)

    def test_change_wall_material(self):
        new_mat = "new_mat"
        self.house.change_wall_material(new_mat)
        self.assertEqual(new_mat, self.house.wallFront.material_id)
        self.assertEqual(new_mat, self.house.wallLeft.material_id)
        self.assertEqual(new_mat, self.house.wallRight.material_id)
        self.assertEqual(new_mat, self.house.wallBack.material_id)
