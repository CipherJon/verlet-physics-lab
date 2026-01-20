# rope_swing.py
# Implementation of a scene demonstrating a swinging rope using position-based dynamics.
# Updated to use Verlet integration with multiple constraint iterations and strong gravity.

import pygame

from core.vector2d import Vector2D
from integration.verlet import VerletIntegrator
from objects.rope import Rope
from rendering.debug_renderer import DebugRenderer


class RopeSwingScene:
    """
    A scene demonstrating a swinging rope using position-based dynamics.
    The rope is anchored at one end and swings freely under gravity.
    This implementation uses Verlet integration with multiple constraint iterations
    for stable, realistic rope physics.
    """

    def __init__(self, num_particles=20, segment_length=10.0, gravity_strength=800.0):
        """
        Initialize the rope swing scene with a number of particles and segment length.

        Args:
            num_particles (int, optional): The number of particles in the rope. Defaults to 20.
            segment_length (float, optional): The length of each segment in the rope. Defaults to 10.0.
            gravity_strength (float, optional): The strength of gravity in pixel units. Defaults to 800.0.
        """
        self.num_particles = num_particles
        self.segment_length = segment_length
        self.gravity_strength = gravity_strength
        self.rope = None
        self.renderer = None
        self.integrator = None

    def setup(self):
        """
        Set up the scene by creating the rope, renderer, and integrator.
        """
        # Create the rope
        start_position = Vector2D(400, 100)
        self.rope = Rope(start_position, self.num_particles, self.segment_length)

        # Create the renderer
        self.renderer = DebugRenderer(width=800, height=600)

        # Create the integrator with constraints and proper physics parameters
        gravity = Vector2D(0, self.gravity_strength)
        self.integrator = VerletIntegrator(
            self.rope.particles,
            constraints=self.rope.constraints,
            constraint_iterations=10,
            damping=0.99,
            gravity=gravity,
        )

    def run(self):
        """
        Run the simulation loop for the rope swing scene.
        """
        self.setup()

        running = True
        frame_count = 0
        clock = pygame.time.Clock()

        while running:
            # Handle events at the beginning of the loop
            running = self.renderer.handle_events()
            if not running:
                print("Exiting simulation loop...")
                break

            # Log frame count
            frame_count += 1
            if frame_count % 100 == 0:
                print(f"Frame {frame_count}: Running simulation...")

            # Clear the screen
            self.renderer.clear()

            # Update physics using Verlet integration with PBD
            # Gravity is now handled by the integrator, not applied here
            self.integrator.integrate(0.016)  # Fixed time step of ~60fps

            # Render the rope
            self.rope.render(self.renderer)

            # Update the display
            self.renderer.render()

            # Cap the frame rate for consistent simulation
            clock.tick(60)

    def __repr__(self):
        return f"RopeSwingScene(num_particles={self.num_particles}, segment_length={self.segment_length}, gravity_strength={self.gravity_strength})"
