#!/usr/bin/python3
"""test for BaseModel"""
from models import storage
import unittest
import os
from os import getenv
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "__repr__"))
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))
        new_base = BaseModel({'name': "California"})

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "fails with DB")
    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertNotIn("_sa_instance_state", base_dict.keys())
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "fails with DB")
    def test_delete_BaseModel(self):
        """test delete method of BaseModel"""
        new_base = BaseModel()
        new_base.save()
        countb = len(storage.all().keys())
        new_base.delete()
        counta = len(storage.all().keys())
        self.assertGreater(countb, counta)

if __name__ == "__main__":
    unittest.main()
