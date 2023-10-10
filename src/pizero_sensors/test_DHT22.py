import os, sys, unittest

from DHT22 import DHT22

class TestDHT22(unittest.TestCase):

    def test_GetData(self):
        data = DHT22().get_data()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
