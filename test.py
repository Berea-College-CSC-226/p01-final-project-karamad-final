import unittest
from balloon_class import Balloon  # Ensure this matches the actual file name

class TestBalloon(unittest.TestCase):
    def setUp(self):
        """Set up a Balloon instance for testing."""
        self.balloon = Balloon(x=50, y=50, speed=5, color=(255, 0, 0))  # Red balloon

    def test_move(self):
        """Test if the balloon moves downward correctly."""
        self.balloon.move()
        self.assertEqual(self.balloon.y, 55, "The balloon did not move correctly.")

    def test_is_clicked(self):
        """Test if the is_clicked method works correctly."""
        inside_click = (50, 50)  # Inside the balloon
        outside_click = (100, 100)  # Outside the balloon
        self.assertTrue(self.balloon.is_clicked(inside_click), "is_clicked failed for a click inside the balloon.")
        self.assertFalse(self.balloon.is_clicked(outside_click), "is_clicked failed for a click outside the balloon.")


if __name__ == "__main__":
    unittest.main()
