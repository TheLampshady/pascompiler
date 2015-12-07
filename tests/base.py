import unittest
import json


class TestBase(unittest.TestCase):
    def setUp(self):
        pass

    def print_dict(self, value):
        print json.dumps(value.symbol_table, indent=2)
