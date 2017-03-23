import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Review()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

    def tearDown(self):
        self.cli.do_destroy("Review " + self.model.id)


if __name__ == "__main__":
    unittest.main()
