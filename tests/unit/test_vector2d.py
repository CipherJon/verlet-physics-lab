# test_vector2d.py
# Unit tests for the Vector2D class.

import unittest

from core.vector2d import Vector2D


class TestVector2D(unittest.TestCase):
    """
    Unit tests for the Vector2D class.
    """

    def test_initialization(self):
        """
        Test the initialization of a Vector2D object.
        """
        vector = Vector2D(3.0, 4.0)
        self.assertEqual(vector.x, 3.0)
        self.assertEqual(vector.y, 4.0)

    def test_default_initialization(self):
        """
        Test the default initialization of a Vector2D object.
        """
        vector = Vector2D()
        self.assertEqual(vector.x, 0.0)
        self.assertEqual(vector.y, 0.0)

    def test_addition(self):
        """
        Test the addition of two Vector2D objects.
        """
        vector1 = Vector2D(1.0, 2.0)
        vector2 = Vector2D(3.0, 4.0)
        result = vector1 + vector2
        self.assertEqual(result.x, 4.0)
        self.assertEqual(result.y, 6.0)

    def test_subtraction(self):
        """
        Test the subtraction of two Vector2D objects.
        """
        vector1 = Vector2D(5.0, 6.0)
        vector2 = Vector2D(1.0, 2.0)
        result = vector1 - vector2
        self.assertEqual(result.x, 4.0)
        self.assertEqual(result.y, 4.0)

    def test_multiplication(self):
        """
        Test the multiplication of a Vector2D object by a scalar.
        """
        vector = Vector2D(2.0, 3.0)
        result = vector * 2.0
        self.assertEqual(result.x, 4.0)
        self.assertEqual(result.y, 6.0)

    def test_division(self):
        """
        Test the division of a Vector2D object by a scalar.
        """
        vector = Vector2D(4.0, 6.0)
        result = vector / 2.0
        self.assertEqual(result.x, 2.0)
        self.assertEqual(result.y, 3.0)

    def test_negation(self):
        """
        Test the negation of a Vector2D object.
        """
        vector = Vector2D(3.0, 4.0)
        result = -vector
        self.assertEqual(result.x, -3.0)
        self.assertEqual(result.y, -4.0)

    def test_magnitude(self):
        """
        Test the magnitude calculation of a Vector2D object.
        """
        vector = Vector2D(3.0, 4.0)
        self.assertAlmostEqual(vector.magnitude(), 5.0)

    def test_normalize(self):
        """
        Test the normalization of a Vector2D object.
        """
        vector = Vector2D(3.0, 4.0)
        normalized = vector.normalize()
        self.assertAlmostEqual(normalized.magnitude(), 1.0)

    def test_dot_product(self):
        """
        Test the dot product of two Vector2D objects.
        """
        vector1 = Vector2D(1.0, 2.0)
        vector2 = Vector2D(3.0, 4.0)
        self.assertEqual(vector1.dot(vector2), 11.0)

    def test_repr(self):
        """
        Test the string representation of a Vector2D object.
        """
        vector = Vector2D(3.0, 4.0)
        self.assertEqual(repr(vector), "Vector2D(3.0, 4.0)")

    def test_invalid_initialization(self):
        """
        Test that invalid initialization raises an error.
        """
        with self.assertRaises(TypeError):
            Vector2D("invalid_x", "invalid_y")

    def test_invalid_operations(self):
        """
        Test that invalid operations raise errors.
        """
        vector = Vector2D(3.0, 4.0)
        with self.assertRaises(TypeError):
            vector + "invalid_vector"
        with self.assertRaises(TypeError):
            vector * "invalid_scalar"

    def test_zero_vector(self):
        """
        Test operations on a zero vector.
        """
        zero_vector = Vector2D(0.0, 0.0)
        self.assertEqual(zero_vector.magnitude(), 0.0)
        with self.assertRaises(ZeroDivisionError):
            zero_vector.normalize()

    def test_extreme_values(self):
        """
        Test operations with extreme values.
        """
        extreme_vector = Vector2D(1e10, 1e10)
        self.assertAlmostEqual(extreme_vector.magnitude(), 1.41421356237e10, places=1)


if __name__ == "__main__":
    unittest.main()
