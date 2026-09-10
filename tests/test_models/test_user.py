#!/usr/bin/python3
"""Unittest module for User."""

import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User."""

    def test_user_instance(self):
        """Test that User is an instance of User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_inherits_from_base_model(self):
        """Test that User inherits BaseModel attributes."""
        user = User()

        self.assertIsInstance(user.id, str)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_attributes(self):
        """Test default User attributes."""
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_are_strings(self):
        """Test User default attributes are strings."""
        user = User()

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_custom_attributes(self):
        """Test assigning values to User attributes."""
        user = User()

        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
