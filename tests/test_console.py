import unittest
from console import HBNBCommand

class test_console(unittest.TestCase):

        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "HBNBCommand"
            self.value = HBNBCommand

        def test_prompt(self):
            """testing promt"""
            new = self.value()
            self.assertEqual(new.prompt, "(hbnb)")