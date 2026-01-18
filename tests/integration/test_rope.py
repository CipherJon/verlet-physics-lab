# test_rope.py
# Integration tests for the Rope class.

import unittest

from src.core.vector2d import Vector2D
from src.objects.rope import Rope


class TestRope(unittest.TestCase):
    """
    Integration tests for the Rope class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.start_position = Vector2D(0, 0)
        self.num_particles = 10
        self.segment_length = 5.0
        self.rope = Rope(self.start_position, self.num_particles, self.segment_length)

    def test_initialization(self):
        """
        Test that the rope is initialized correctly.
        """
        self.assertEqual(len(self.rope.particles), self.num_particles)
        self.assertEqual(len(self.rope.springs), self.num_particles - 1)

    def test_update(self):
        """
        Test that the rope updates correctly.
        """
        initial_positions = [
            particle.position.copy() for particle in self.rope.particles
        ]
        self.rope.update(0.016)
        for i, particle in enumerate(self.rope.particles):
            if not particle.is_fixed:
                self.assertNotEqual(particle.position, initial_positions[i])

    def test_render(self):
        """
        Test that the rope renders correctly.
        """

        # Mock renderer for testing
        class MockRenderer:
            def draw_line(self, start, end):
                pass

            def draw_point(self, position):
                pass

        renderer = MockRenderer()
        self.rope.render(renderer)


if __name__ == "__main__":
    unittest.main()
