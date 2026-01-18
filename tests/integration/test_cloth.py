# test_cloth.py
# Integration tests for the Cloth class.

import unittest

from src.core.vector2d import Vector2D
from src.objects.cloth import Cloth


class TestCloth(unittest.TestCase):
    """
    Integration tests for the Cloth class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.cloth = Cloth(width=5, height=5)

    def test_initialization(self):
        """
        Test that the cloth is initialized correctly.
        """
        self.assertEqual(len(self.cloth.particles), 25)  # 5x5 grid
        self.assertGreater(len(self.cloth.springs), 0)  # Should have springs

    def test_update(self):
        """
        Test that the cloth updates correctly.
        """
        initial_positions = [
            particle.position.copy() for particle in self.cloth.particles
        ]
        self.cloth.update(0.016)  # Update with a small time step
        for i, particle in enumerate(self.cloth.particles):
            if not particle.is_fixed:
                self.assertNotEqual(particle.position, initial_positions[i])

    def test_render(self):
        """
        Test that the cloth renders without errors.
        """

        class MockRenderer:
            def draw_line(self, start, end):
                pass

            def draw_point(self, position):
                pass

        renderer = MockRenderer()
        self.cloth.render(renderer)  # Should not raise any errors


if __name__ == "__main__":
    unittest.main()
