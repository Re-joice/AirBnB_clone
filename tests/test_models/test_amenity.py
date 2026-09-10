#!/usr/bin/python3
"""Unittest module for Amenity."""

import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def test_amenity_instance(self):
        """Test that Amenity is an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_inherits_from_base_model(self):
        """Test that Amenity inherits BaseModel attributes."""
        amenity = Amenity()

        self.assertIsInstance(amenity.id, str)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_amenity_name(self):
        """Test default name attribute."""
        amenity = Amenity()

        self.assertEqual(amenity.name, "")
        self.assertIsInstance(amenity.name, str)

    def test_amenity_custom_name(self):
        """Test assigning a custom name."""
        amenity = Amenity()
        amenity.name = "WiFi"

        self.assertEqual(amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()
