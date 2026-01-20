# test_rope_swing.py
# A test script to verify the rope swing simulation.

import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent))

try:
    import pygame

    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from src.core.vector2d import Vector2D
from src.integration.verlet import VerletIntegrator
from src.objects.rope import Rope


def test_rope_swing():
    """
    Test the rope swing simulation.
    """
    if not PYGAME_AVAILABLE:
        print("PyGame not available, skipping test")
        return

    # Initialize PyGame (but avoid opening a window)
    pygame.init()

    # Create the rope
    start_position = Vector2D(400, 100)
    rope = Rope(start_position, 3, 10.0)

    # Create the integrator
    integrator = VerletIntegrator(rope.particles)

    # Run the simulation for a fixed number of steps
    for i in range(100):
        # Apply gravity to the rope
        for particle in rope.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))

        # Update the rope
        integrator.integrate(0.001)

    # Quit PyGame
    pygame.quit()

    print("Rope swing simulation successful")


def test_rope_swing_with_headless_rendering():
    """
    Test the rope swing simulation with headless rendering using matplotlib.
    """
    try:
        import matplotlib

        matplotlib.use("Agg")  # Use a non-interactive backend
        import matplotlib.pyplot as plt

        from src.rendering.matplotlib_renderer import MatplotlibRenderer

        HEADLESS_RENDERING_AVAILABLE = True
    except ImportError:
        print("Matplotlib not available, skipping headless rendering test")
        return

    # Create the rope
    start_position = Vector2D(400, 100)
    rope = Rope(start_position, 3, 10.0)

    # Create the integrator
    integrator = VerletIntegrator(rope.particles)

    # Create the renderer
    renderer = MatplotlibRenderer()

    # Run the simulation for a fixed number of steps
    for i in range(100):
        # Apply gravity to the rope
        for particle in rope.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))

        # Update the rope
        integrator.integrate(0.001)

        # Render the rope
        renderer.draw_line(rope.particles[0].position, rope.particles[1].position)
        renderer.draw_line(rope.particles[1].position, rope.particles[2].position)

    # Close the renderer
    renderer.close()

    print("Rope swing simulation with headless rendering successful")


if __name__ == "__main__":
    test_rope_swing()
    test_rope_swing_with_headless_rendering()
