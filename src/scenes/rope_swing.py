# rope_swing.py
# Implementation of a scene demonstrating a swinging rope.

from ..core.vector2d import Vector2D
from ..integration.verlet import VerletIntegrator
from ..objects.rope import Rope
from ..rendering.debug_renderer import DebugRenderer


class RopeSwingScene:
    """
    A scene demonstrating a swinging rope.
    The rope is anchored at one end and swings freely under gravity.
    """

    def __init__(self, num_particles=20, segment_length=10.0):
        """
        Initialize the rope swing scene with a number of particles and segment length.

        Args:
            num_particles (int, optional): The number of particles in the rope. Defaults to 20.
            segment_length (float, optional): The length of each segment in the rope. Defaults to 10.0.
        """
        self.num_particles = num_particles
        self.segment_length = segment_length
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

        # Create the integrator
        self.integrator = VerletIntegrator(self.rope.particles)

    def run(self):
        """
        Run the simulation loop for the rope swing scene.
        """
        self.setup()

        running = True
        while running:
            # Handle events
            running = self.renderer.handle_events()

            # Clear the screen
            self.renderer.clear()

            # Apply gravity to the rope
            for particle in self.rope.particles:
                if not particle.is_fixed:
                    particle.apply_force(Vector2D(0, 9.81))

            # Update the rope
            self.integrator.integrate(0.016)  # Fixed time step

            # Render the rope
            self.rope.render(self.renderer)

            # Update the display
            self.renderer.render()

    def __repr__(self):
        return f"RopeSwingScene(num_particles={self.num_particles}, segment_length={self.segment_length})"
