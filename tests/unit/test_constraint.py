# test_constraint.py
# Unit tests for the Constraint class.

import unittest

from src.core.constraint import Constraint
from src.core.particle import Particle
from src.core.vector2d import Vector2D


class TestConstraint(unittest.TestCase):
    """
    Unit tests for the Constraint class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.particle1 = Particle(Vector2D(0, 0), 1.0, False)
        self.particle2 = Particle(Vector2D(1, 1), 1.0, False)
        self.constraint = Constraint(self.particle1, self.particle2, 1.0)

    def test_constraint_initialization(self):
        """
        Test the initialization of the Constraint class.
        """
        self.assertEqual(self.constraint.particle1, self.particle1)
        self.assertEqual(self.constraint.particle2, self.particle2)
        self.assertEqual(self.constraint.rest_length, 1.0)

    def test_constraint_satisfy(self):
        """
        Test that the constraint satisfies correctly.
        """
        self.constraint.satisfy()
        distance = self.particle1.position.distance_to(self.particle2.position)
        self.assertAlmostEqual(distance, self.constraint.rest_length, places=5)


if __name__ == "__main__":
    unittest.main()
