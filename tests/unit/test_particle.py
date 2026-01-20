# test_particle.py
# Unit tests for the Particle class.

import unittest

from src.core.particle import Particle
from src.core.vector2d import Vector2D


class TestParticle(unittest.TestCase):
    """
    Unit tests for the Particle class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.position = Vector2D(0, 0)
        self.particle = Particle(self.position, mass=1.0, is_fixed=False)

    def test_initialization(self):
        """
        Test that the particle is initialized correctly.
        """
        self.assertEqual(self.particle.position, self.position)
        self.assertEqual(self.particle.old_position, self.position)
        self.assertEqual(self.particle.acceleration, Vector2D(0, 0))
        self.assertEqual(self.particle.mass, 1.0)
        self.assertEqual(self.particle.inv_mass, 1.0)
        self.assertFalse(self.particle.is_fixed)

    def test_apply_force(self):
        """
        Test that applying a force updates the acceleration correctly.
        """
        force = Vector2D(10, 20)
        self.particle.apply_force(force)
        self.assertEqual(self.particle.acceleration, force)

    def test_apply_force_fixed_particle(self):
        """
        Test that applying a force to a fixed particle does not update the acceleration.
        """
        fixed_particle = Particle(self.position, mass=1.0, is_fixed=True)
        force = Vector2D(10, 20)
        fixed_particle.apply_force(force)
        self.assertEqual(fixed_particle.acceleration, Vector2D(0, 0))

    def test_update_position(self):
        """
        Test that updating the position works correctly.
        """
        initial_position = self.particle.position.copy()
        self.particle.acceleration = Vector2D(10, 20)
        self.particle.update_position(0.1)
        self.assertNotEqual(self.particle.position, initial_position)

    def test_update_position_fixed_particle(self):
        """
        Test that updating the position of a fixed particle does not change its position.
        """
        fixed_particle = Particle(self.position, mass=1.0, is_fixed=True)
        fixed_particle.acceleration = Vector2D(10, 20)
        fixed_particle.update_position(0.1)
        self.assertEqual(fixed_particle.position, self.position)

    def test_repr(self):
        """
        Test the string representation of the particle.
        """
        self.assertEqual(
            repr(self.particle),
            "Particle(position=Vector2D(0, 0), mass=1.0, is_fixed=False)",
        )

    def test_negative_mass_particle(self):
        """
        Test that a particle with negative mass raises an error.
        """
        with self.assertRaises(ValueError):
            Particle(self.position, mass=-1.0, is_fixed=False)

    def test_invalid_force_application(self):
        """
        Test that applying an invalid force (non-Vector2D) raises an error.
        """
        with self.assertRaises(TypeError):
            self.particle.apply_force("invalid_force")

    def test_zero_mass_particle(self):
        """
        Test that a particle with zero mass is handled correctly.
        """
        zero_mass_particle = Particle(self.position, mass=0.0, is_fixed=False)
        self.assertEqual(zero_mass_particle.mass, 0.0)
        self.assertEqual(zero_mass_particle.inv_mass, float("inf"))

    def test_extreme_force_application(self):
        """
        Test that applying an extreme force updates the acceleration correctly.
        """
        extreme_force = Vector2D(1e6, 1e6)
        self.particle.apply_force(extreme_force)
        self.assertEqual(self.particle.acceleration, extreme_force)


if __name__ == "__main__":
    unittest.main()
