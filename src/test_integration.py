from core.vector2d import Vector2D
from integration.verlet import VerletIntegrator
from objects.rope import Rope


def test_integration():
    # Create a rope with 3 particles
    rope = Rope(Vector2D(400, 100), 3, 10.0)

    # Create the integrator
    integrator = VerletIntegrator(rope.particles)

    # Run the integration for 100 steps
    for i in range(100):
        integrator.integrate(0.016)

    print("Integration successful")


if __name__ == "__main__":
    test_integration()
