# test_chain.py
import unittest

from src.core.particle import Particle
from src.core.spring import Spring
from src.objects.chain import Chain


class TestChain(unittest.TestCase):
    def setUp(self):
        self.chain = Chain(
            particle_count=5,
            particle_mass=1.0,
            spring_stiffness=0.5,
            spring_damping=0.1,
        )

    def test_chain_initialization(self):
        self.assertEqual(len(self.chain.particles), 5)
        self.assertEqual(len(self.chain.springs), 4)

    def test_chain_update(self):
        initial_positions = [p.position for p in self.chain.particles]
        self.chain.update(0.016)
        final_positions = [p.position for p in self.chain.particles]
        self.assertNotEqual(initial_positions, final_positions)

    def test_invalid_chain_initialization(self):
        """
        Test that invalid chain initialization raises an error.
        """
        with self.assertRaises(ValueError):
            Chain(
                particle_count=0,
                particle_mass=1.0,
                spring_stiffness=0.5,
                spring_damping=0.1,
            )

    def test_chain_performance(self):
        import time

        start_time = time.time()
        for _ in range(100):
            self.chain.update(0.016)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Chain update performance: {elapsed_time:.4f} seconds for 100 iterations"
        )
        self.assertLess(elapsed_time, 1.0)  # Should complete in under 1 second


if __name__ == "__main__":
    unittest.main()
