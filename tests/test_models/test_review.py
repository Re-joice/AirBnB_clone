#!/usr/bin/python3
"""Unittest module for Review."""

import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    def test_review_instance(self):
        """Test that Review is an instance of Review."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_inherits_from_base_model(self):
        """Test that Review inherits BaseModel attributes."""
        review = Review()

        self.assertIsInstance(review.id, str)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_default_attributes(self):
        """Test default Review attributes."""
        review = Review()

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_types(self):
        """Test default Review attribute types."""
        review = Review()

        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_custom_attributes(self):
        """Test assigning custom Review attributes."""
        review = Review()

        review.place_id = "place-123"
        review.user_id = "user-123"
        review.text = "Great place!"

        self.assertEqual(review.place_id, "place-123")
        self.assertEqual(review.user_id, "user-123")
        self.assertEqual(review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()
