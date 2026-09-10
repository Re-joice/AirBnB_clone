#!/usr/bin/python3
"""Unittest module for BaseModel."""

import unittest
from datetime import datetime
from unittest.mock import patch

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_id(self):
        """Test that every instance has a unique string id."""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """Test created_at is a datetime."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at is a datetime."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        model = BaseModel()
        model.name = "My Model"

        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertNotIn("__class__", new_model.__dict__)

    def test_init_with_kwargs_ignores_class(self):
        """Test that __class__ is ignored during initialization."""
        model = BaseModel(
            id="123",
            created_at="2020-01-01T12:00:00",
            updated_at="2020-01-01T12:00:00",
            __class__="WrongClass"
        )

        self.assertEqual(model.id, "123")
        self.assertNotIn("__class__", model.__dict__)

    def test_init_no_kwargs(self):
        """Test initialization without keyword arguments."""
        model = BaseModel()

        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()

        expected = "[BaseModel] ({}) {}".format(
            model.id, model.__dict__
        )

        self.assertEqual(str(model), expected)

    def test_save(self):
        """Test that save updates updated_at and calls storage.save."""
        model = BaseModel()
        old_updated_at = model.updated_at

        with patch("models.base_model.storage.save") as mock_save:
            model.save()

            mock_save.assert_called_once()

        self.assertGreaterEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the dictionary representation."""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89

        model_dict = model.to_dict()

        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_to_dict_does_not_modify_object(self):
        """Test that to_dict does not modify the instance."""
        model = BaseModel()
        model.name = "Test"

        model.to_dict()

        self.assertNotIn("__class__", model.__dict__)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
