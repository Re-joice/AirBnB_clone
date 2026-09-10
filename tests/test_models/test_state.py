#!/usr/bin/python3
"""Unittest module for State."""

import unittest

from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    def test_state_instance(self):
        """Test that State is an instance of State."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_inherits_from_base_model(self):
        """Test that State inherits BaseModel attributes."""
        state = State()

        self.assertIsInstance(state.id, str)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_state_name(self):
        """Test default name attribute."""
        state = State()

        self.assertEqual(state.name, "")
        self.assertIsInstance(state.name, str)

    def test_state_custom_name(self):
        """Test assigning a custom name."""
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")


if __name__ == "__main__":
    unittest.main()
