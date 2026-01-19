# test_simulation.py
# A test script to verify the simulation without rendering.

import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent))

from core.vector2d import Vector2D
from integration.verlet import VerletIntegrator
from objects.rope import Rope


def test_simulation():
    """
    Test the simulation without rendering.
    """
    # Create a rope with 3 particles
    rope = Rope(Vector2D(400, 100), 3, 10.0)

    # Create the integrator
    integrator = VerletIntegrator(rope.particles)

    # Run the simulation for 100 steps
    for i in range(100):
        # Apply gravity to the rope
        for particle in rope.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))

        # Update the rope
        integrator.integrate(0.016)

    print("Simulation successful")


if __name__ == "__main__":
    test_simulation()
