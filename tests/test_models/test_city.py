import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_CityModel(unittest.TestCase):
    """
    Test the city model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = City()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")

    def tearDown(self):
        self.cli.do_destroy("City " + self.model.id)


if __name__ == "__main__":
    unittest.main()
