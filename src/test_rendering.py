# test_rendering.py
# A test script to verify the simulation with rendering.

from core.vector2d import Vector2D
from integration.verlet import VerletIntegrator
from objects.rope import Rope
from rendering.debug_renderer import DebugRenderer


def test_rendering():
    """
    Test the simulation with rendering.
    """
    # Create a rope with 3 particles
    rope = Rope(Vector2D(400, 100), 3, 10.0)

    # Create the renderer
    renderer = DebugRenderer(width=800, height=600)

    # Create the integrator
    integrator = VerletIntegrator(rope.particles)

    # Run the simulation for 100 steps
    for i in range(100):
        # Handle events
        running = renderer.handle_events()
        if not running:
            break

        # Clear the screen
        renderer.clear()

        # Apply gravity to the rope
        for particle in rope.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))

        # Update the rope
        integrator.integrate(0.016)

        # Render the rope
        rope.render(renderer)

        # Update the display
        renderer.render()

    print("Rendering successful")


if __name__ == "__main__":
    test_rendering()
