#!/usr/bin/python3
"""Unittest module for City."""

import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City."""

    def test_city_instance(self):
        """Test that City is an instance of City."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_inherits_from_base_model(self):
        """Test that City inherits BaseModel attributes."""
        city = City()

        self.assertIsInstance(city.id, str)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_attributes(self):
        """Test default City attributes."""
        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_custom_attributes(self):
        """Test assigning custom City attributes."""
        city = City()
        city.state_id = "1234"
        city.name = "Accra"

        self.assertEqual(city.state_id, "1234")
        self.assertEqual(city.name, "Accra")


if __name__ == "__main__":
    unittest.main()
