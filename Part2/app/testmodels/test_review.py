from ..models.review import Review
import unittest

class TestUser(unittest.TestCase):
    def test_review_creation(self):
        review = Review(name="Wi-Fi")
        self.assertEqual(review.name, "Wi-Fi")


if __name__ == "__main__":
    unittest.main()