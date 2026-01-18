# test_ragdoll.py
# Integration tests for the Ragdoll class.

import unittest

from src.core.vector2d import Vector2D
from src.objects.ragdoll import Ragdoll


class TestRagdoll(unittest.TestCase):
    """
    Integration tests for the Ragdoll class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.position = Vector2D(400, 300)
        self.ragdoll = Ragdoll(self.position, limb_length=20.0)

    def test_initialization(self):
        """
        Test that the ragdoll is initialized correctly.
        """
        self.assertEqual(len(self.ragdoll.particles), 6)
        self.assertEqual(len(self.ragdoll.springs), 5)

    def test_update(self):
        """
        Test that the ragdoll updates correctly.
        """
        initial_positions = [
            particle.position.copy() for particle in self.ragdoll.particles
        ]
        self.ragdoll.update(0.016)
        for i, particle in enumerate(self.ragdoll.particles):
            if not particle.is_fixed:
                self.assertNotEqual(particle.position, initial_positions[i])

    def test_apply_forces(self):
        """
        Test that forces are applied correctly to the ragdoll.
        """
        initial_accelerations = [
            particle.acceleration.copy() for particle in self.ragdoll.particles
        ]
        self.ragdoll.apply_forces()
        for i, particle in enumerate(self.ragdoll.particles):
            if not particle.is_fixed:
                self.assertNotEqual(particle.acceleration, initial_accelerations[i])


if __name__ == "__main__":
    unittest.main()
