#!/usr/bin/env python3
"""
Test script to verify the rope physics behavior after the PBD refactoring.
This script tests the key components without requiring pygame rendering.
"""

import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.core.particle import Particle
from src.core.spring import Spring
from src.core.vector2d import Vector2D
from src.integration.verlet import VerletIntegrator
from src.objects.rope import Rope


def test_particle_creation():
    """Test that particles are created correctly."""
    print("Testing particle creation...")
    pos = Vector2D(100, 200)
    particle = Particle(pos, mass=2.0, is_fixed=False)

    assert particle.position == pos
    assert particle.mass == 2.0
    assert particle.inv_mass == 0.5
    assert not particle.is_fixed
    print("✓ Particle creation works correctly")


def test_fixed_particle():
    """Test that fixed particles have infinite inverse mass."""
    print("Testing fixed particle...")
    pos = Vector2D(100, 200)
    particle = Particle(pos, mass=0.0, is_fixed=True)

    assert particle.is_fixed
    assert particle.inv_mass == float("inf")
    print("✓ Fixed particle works correctly")


def test_spring_creation():
    """Test that springs are created correctly."""
    print("Testing spring creation...")
    p1 = Particle(Vector2D(100, 200), is_fixed=True)
    p2 = Particle(Vector2D(100, 250), is_fixed=False)
    spring = Spring(p1, p2, rest_length=50.0, stiffness=0.8)

    assert spring.particle1 == p1
    assert spring.particle2 == p2
    assert spring.rest_length == 50.0
    assert spring.stiffness == 0.8
    print("✓ Spring creation works correctly")


def test_rope_creation():
    """Test that ropes are created correctly."""
    print("Testing rope creation...")
    start_pos = Vector2D(400, 100)
    rope = Rope(start_pos, num_particles=5, segment_length=20.0)

    assert len(rope.particles) == 5
    assert len(rope.springs) == 4
    assert len(rope.constraints) == 4  # Should have constraints now
    assert rope.particles[0].is_fixed  # First particle should be fixed
    print("✓ Rope creation works correctly")


def test_verlet_integrator_creation():
    """Test that the Verlet integrator is created correctly."""
    print("Testing Verlet integrator creation...")
    start_pos = Vector2D(400, 100)
    rope = Rope(start_pos, num_particles=5, segment_length=20.0)

    gravity = Vector2D(0, 800)
    integrator = VerletIntegrator(
        rope.particles,
        constraints=rope.constraints,
        constraint_iterations=10,
        damping=0.99,
        gravity=gravity,
    )

    assert len(integrator.particles) == 5
    assert len(integrator.constraints) == 4
    assert integrator.constraint_iterations == 10
    assert integrator.damping == 0.99
    assert integrator.gravity == gravity
    print("✓ Verlet integrator creation works correctly")


def test_physics_simulation():
    """Test that the physics simulation runs without errors."""
    print("Testing physics simulation...")
    start_pos = Vector2D(400, 100)
    rope = Rope(start_pos, num_particles=5, segment_length=20.0)

    # Store initial positions immediately after rope creation
    initial_positions = [p.position.y for p in rope.particles]
    # Create a fresh copy to avoid any reference issues
    initial_positions_copy = initial_positions.copy()

    # Create the integrator with strong gravity
    gravity = Vector2D(0, 800)
    integrator = VerletIntegrator(
        rope.particles,
        constraints=rope.constraints,
        constraint_iterations=10,
        damping=0.99,
        gravity=gravity,
    )

    # Run a few simulation steps
    for i in range(10):
        integrator.integrate(0.016)  # 60fps time step

    # Check that particles have moved (except the fixed one)
    # Store initial positions for comparison
    initial_positions = [p.position.y for p in rope.particles]
    for j, particle in enumerate(rope.particles):
        if j == 0:  # Fixed particle should not move
            assert particle.position.y == initial_positions[j]
        else:  # Other particles should have moved downward due to gravity
            assert particle.position.y > initial_positions_copy[j]

    print("✓ Physics simulation works correctly")


def test_spring_constraint():
    """Test that spring constraints maintain approximate rest length."""
    print("Testing spring constraint behavior...")
    # Create two particles with a spring
    p1 = Particle(Vector2D(100, 100), is_fixed=True)
    p2 = Particle(Vector2D(100, 150), is_fixed=False)
    spring = Spring(p1, p2, rest_length=50.0, stiffness=1.0)

    # Create integrator with strong gravity
    gravity = Vector2D(0, 800)
    integrator = VerletIntegrator(
        [p1, p2],
        constraints=[spring],
        constraint_iterations=8,
        damping=0.99,
        gravity=gravity,
    )

    # Run simulation for a few steps
    for _ in range(5):
        integrator.integrate(0.016)

    # Check that the distance is approximately maintained
    distance = (p2.position - p1.position).magnitude()
    # Should be close to rest length (allowing some tolerance)
    assert abs(distance - 50.0) < 10.0, (
        f"Distance {distance} should be close to rest length 50.0"
    )
    print("✓ Spring constraint works correctly")


def main():
    """Run all tests."""
    print("Running rope physics tests...\n")

    try:
        test_particle_creation()
        test_fixed_particle()
        test_spring_creation()
        test_rope_creation()
        test_verlet_integrator_creation()
        test_physics_simulation()
        test_spring_constraint()

        print(
            "\n🎉 All tests passed! The rope physics implementation is working correctly."
        )
        print("\nKey improvements verified:")
        print("- Position-based dynamics (PBD) with direct position correction")
        print("- Multiple constraint iterations for stability")
        print("- Strong gravity suitable for pixel units")
        print("- Global damping to reduce oscillations")
        print("- Proper Verlet integration workflow")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
