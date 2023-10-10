import os, sys, unittest

from CPUTemp import CPUTemp

class TestCPUTemp(unittest.TestCase):

    def test_GetData(self):
        data = CPUTemp().get_data()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
