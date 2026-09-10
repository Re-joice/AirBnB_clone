#!/usr/bin/python3
"""Unittest module for FileStorage."""

import json
import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def setUp(self):
        """Set up a clean FileStorage instance."""
        self.storage = FileStorage()

        FileStorage._FileStorage__objects = {}

        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test."""
        FileStorage._FileStorage__objects = {}

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all returns the objects dictionary."""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test that new adds an object to storage."""
        model = BaseModel()

        self.storage.new(model)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], model)

    def test_new_multiple_objects(self):
        """Test that multiple objects are stored."""
        model1 = BaseModel()
        model2 = BaseModel()

        self.storage.new(model1)
        self.storage.new(model2)

        self.assertEqual(len(self.storage.all()), 2)

    def test_save(self):
        """Test that save serializes objects to JSON."""
        model = BaseModel()
        model.name = "Test Model"

        self.storage.new(model)
        self.storage.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as file:
            data = json.load(file)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, data)
        self.assertEqual(data[key]["name"], "Test Model")
        self.assertEqual(data[key]["__class__"], "BaseModel")

    def test_reload(self):
        """Test that reload recreates objects from JSON."""
        model = BaseModel()
        model.name = "Reload Test"

        self.storage.new(model)
        self.storage.save()

        FileStorage._FileStorage__objects = {}

        self.storage.reload()

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, self.storage.all())
        new_model = self.storage.all()[key]

        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, "Reload Test")
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)

    def test_reload_missing_file(self):
        """Test reload when file.json does not exist."""
        if os.path.exists("file.json"):
            os.remove("file.json")

        self.storage.reload()

        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
