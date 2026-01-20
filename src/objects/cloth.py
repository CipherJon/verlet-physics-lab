# cloth.py
# Implementation of a simple grid-based cloth for the physics simulation.

from core.particle import Particle
from core.spring import Spring
from core.vector2d import Vector2D


class Cloth:
    """
    A class representing a simple grid-based cloth in the simulation.
    The cloth is modeled as a grid of particles connected by springs.
    """

    def __init__(
        self, width, height, particle_mass=1.0, spring_stiffness=1.0, spring_damping=0.1
    ):
        """
        Initialize the cloth with a grid of particles and springs.

        Args:
            width (int): The number of particles along the width of the cloth.
            height (int): The number of particles along the height of the cloth.
            particle_mass (float, optional): The mass of each particle. Defaults to 1.0.
            spring_stiffness (float, optional): The stiffness of the springs. Defaults to 1.0.
            spring_damping (float, optional): The damping factor of the springs. Defaults to 0.1.

        Raises:
            ValueError: If width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height
        self.particles = []
        self.springs = []

        # Create particles in a grid
        for y in range(height):
            for x in range(width):
                position = Vector2D(x, y)
                particle = Particle(position, particle_mass)
                self.particles.append(particle)

        # Create springs between particles
        for y in range(height):
            for x in range(width):
                # Horizontal springs
                if x < width - 1:
                    particle1 = self.particles[y * width + x]
                    particle2 = self.particles[y * width + (x + 1)]
                    rest_length = 1.0  # Distance between adjacent particles
                    spring = Spring(
                        particle1,
                        particle2,
                        rest_length,
                        spring_stiffness,
                        spring_damping,
                    )
                    self.springs.append(spring)

                # Vertical springs
                if y < height - 1:
                    particle1 = self.particles[y * width + x]
                    particle2 = self.particles[(y + 1) * width + x]
                    rest_length = 1.0  # Distance between adjacent particles
                    spring = Spring(
                        particle1,
                        particle2,
                        rest_length,
                        spring_stiffness,
                        spring_damping,
                    )
                    self.springs.append(spring)

                # Diagonal springs (optional)
                if x < width - 1 and y < height - 1:
                    particle1 = self.particles[y * width + x]
                    particle2 = self.particles[(y + 1) * width + (x + 1)]
                    rest_length = 1.414  # Approximate diagonal distance
                    spring = Spring(
                        particle1,
                        particle2,
                        rest_length,
                        spring_stiffness,
                        spring_damping,
                    )
                    self.springs.append(spring)

    def update(self, delta_time):
        """
        Update the cloth by applying forces and constraints.

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

        # Update particles
        for particle in self.particles:
            particle.update_position(delta_time)

    def render(self, renderer):
        """
        Render the cloth using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the cloth.
        """
        for spring in self.springs:
            renderer.draw_line(spring.particle1.position, spring.particle2.position)

        for particle in self.particles:
            renderer.draw_point(particle.position)

    def __repr__(self):
        return f"Cloth(width={self.width}, height={self.height}, particles={len(self.particles)}, springs={len(self.springs)})"
