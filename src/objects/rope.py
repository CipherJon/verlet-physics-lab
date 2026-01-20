# rope.py
# Implementation of a rope-like structure for the softbody ragdoll simulation.
# Updated to use position-based dynamics with Verlet integration.

from src.core.particle import Particle
from src.core.spring import Spring
from src.core.vector2d import Vector2D


class Rope:
    """
    A class representing a rope-like structure made of particles and springs.
    The rope is a simple chain of particles connected by springs.
    This implementation uses position-based dynamics for stable, realistic simulations.

    Attributes:
        particles (list[Particle]): List of particles in the rope.
        springs (list[Spring]): List of springs connecting the particles.
        constraints (list[Constraint]): List of constraints (currently just springs).
    """

    def __init__(
        self, start_position, num_particles, segment_length, mass_per_particle=1.0
    ):
        """
        Initialize the rope with a starting position, number of particles, and segment length.

        Args:
            start_position (Vector2D): The starting position of the rope.
            num_particles (int): The number of particles in the rope.
            segment_length (float): The length of each segment (distance between particles).
            mass_per_particle (float, optional): The mass of each particle. Defaults to 1.0.
        """
        if num_particles <= 0:
            raise ValueError("Number of particles must be positive.")
        self.particles = []
        self.springs = []

        # Create particles
        for i in range(num_particles):
            position = Vector2D(start_position.x, start_position.y - i * segment_length)
            particle = Particle(position, mass_per_particle, is_fixed=(i == 0))
            self.particles.append(particle)

        # Create springs between particles
        for i in range(num_particles - 1):
            spring = Spring(self.particles[i], self.particles[i + 1], segment_length)
            self.springs.append(spring)

        # Constraints are the same as springs for now
        self.constraints = self.springs

    def update(self, delta_time):
        """
        Update the rope by applying forces and constraints.

        Args:
            delta_time (float): The time step for the update.
        """
        # Apply external forces (e.g., gravity)
        for particle in self.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))  # Apply gravity

        # Apply spring forces
        for spring in self.springs:
            spring.apply()

        # Update particle positions
        for particle in self.particles:
            particle.update_position(delta_time)

    def render(self, renderer):
        """
        Render the rope using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the rope.
        """
        for spring in self.springs:
            renderer.draw_line(spring.particle1.position, spring.particle2.position)

        for particle in self.particles:
            renderer.draw_point(particle.position)

    def __repr__(self):
        return f"Rope(particles={len(self.particles)}, springs={len(self.springs)})"
