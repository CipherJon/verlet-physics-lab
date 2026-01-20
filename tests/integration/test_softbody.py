# test_softbody.py
# Integration tests for the SoftBody class.

import unittest

from src.core.vector2d import Vector2D
from src.objects.softbody import SoftBody


class TestSoftBody(unittest.TestCase):
    """
    Integration tests for the SoftBody class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.position = Vector2D(0, 0)
        self.softbody = SoftBody(
            position=self.position,
            width=100,
            height=100,
            rows=5,
            cols=5,
            particle_mass=1.0,
            spring_stiffness=1.0,
            spring_damping=0.1,
        )

    def test_initialization(self):
        """
        Test that the softbody is initialized correctly.
        """
        self.assertEqual(len(self.softbody.particles), 25)  # 5x5 grid
        self.assertEqual(len(self.softbody.springs), 40)  # 5x5 grid with springs

    def test_apply_force(self):
        """
        Test that applying a force to the softbody works correctly.
        """
        force = Vector2D(0.0, 9.81)  # Gravity
        self.softbody.apply_force(force)

        # Check that the force was applied to all particles
        for particle in self.softbody.particles:
            self.assertEqual(particle.acceleration.x, force.x)
            self.assertEqual(particle.acceleration.y, force.y)

    def test_update(self):
        """
        Test that updating the softbody works correctly.
        """
        initial_positions = [
            particle.position.copy() for particle in self.softbody.particles
        ]
        self.softbody.update(0.016)  # Fixed time step

        # Check that the positions have changed
        for i, particle in enumerate(self.softbody.particles):
            self.assertNotEqual(particle.position, initial_positions[i])

    def test_render(self):
        """
        Test that rendering the softbody does not raise errors.
        """

        # Mock renderer
        class MockRenderer:
            def draw_line(self, start, end):
                pass

            def draw_point(self, position):
                pass

        renderer = MockRenderer()
        self.softbody.render(renderer)

    def test_invalid_softbody_initialization(self):
        """
        Test that invalid softbody initialization raises an error.
        """
        with self.assertRaises(ValueError):
            SoftBody(
                position=self.position,
                width=0,
                height=100,
                rows=5,
                cols=5,
                particle_mass=1.0,
                spring_stiffness=1.0,
                spring_damping=0.1,
            )

    def test_softbody_performance(self):
        import time

        start_time = time.time()
        for _ in range(100):
            self.softbody.update(0.016)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"SoftBody update performance: {elapsed_time:.4f} seconds for 100 iterations"
        )
        self.assertLess(elapsed_time, 1.0)  # Should complete in under 1 second


if __name__ == "__main__":
    unittest.main()
