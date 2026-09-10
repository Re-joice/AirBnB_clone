#!/usr/bin/python3
"""Unittest module for Place."""

import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def test_place_instance(self):
        """Test that Place is an instance of Place."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_inherits_from_base_model(self):
        """Test that Place inherits BaseModel attributes."""
        place = Place()

        self.assertIsInstance(place.id, str)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_place_default_attributes(self):
        """Test default Place attributes."""
        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_types(self):
        """Test default Place attribute types."""
        place = Place()

        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_custom_attributes(self):
        """Test assigning custom Place attributes."""
        place = Place()

        place.city_id = "city-123"
        place.user_id = "user-123"
        place.name = "My House"
        place.description = "A nice place"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 150
        place.latitude = 5.6037
        place.longitude = -0.1870
        place.amenity_ids = ["amenity-1", "amenity-2"]

        self.assertEqual(place.city_id, "city-123")
        self.assertEqual(place.user_id, "user-123")
        self.assertEqual(place.name, "My House")
        self.assertEqual(place.description, "A nice place")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 150)
        self.assertEqual(place.latitude, 5.6037)
        self.assertEqual(place.longitude, -0.1870)
        self.assertEqual(place.amenity_ids, ["amenity-1", "amenity-2"])


if __name__ == "__main__":
    unittest.main()
