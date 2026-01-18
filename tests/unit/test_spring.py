# test_spring.py
# Unit tests for the Spring class.

import unittest

from src.core.particle import Particle
from src.core.spring import Spring
from src.core.vector2d import Vector2D


class TestSpring(unittest.TestCase):
    """
    Unit tests for the Spring class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.particle1 = Particle(Vector2D(0, 0), 1.0, False)
        self.particle2 = Particle(Vector2D(1, 1), 1.0, False)
        self.spring = Spring(self.particle1, self.particle2, 1.0, 0.5, 0.1)

    def test_spring_initialization(self):
        """
        Test the initialization of the Spring class.
        """
        self.assertEqual(self.spring.particle1, self.particle1)
        self.assertEqual(self.spring.particle2, self.particle2)
        self.assertEqual(self.spring.rest_length, 1.0)
        self.assertEqual(self.spring.stiffness, 0.5)
        self.assertEqual(self.spring.damping, 0.1)

    def test_spring_apply(self):
        """
        Test that the spring applies forces correctly.
        """
        initial_positions = [
            self.particle1.position.copy(),
            self.particle2.position.copy(),
        ]
        self.spring.apply()
        self.particle1.update_position(0.016)
        self.particle2.update_position(0.016)
        final_positions = [self.particle1.position, self.particle2.position]
        self.assertNotEqual(initial_positions, final_positions)


if __name__ == "__main__":
    unittest.main()
