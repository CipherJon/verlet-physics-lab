# softbody.py
# Implementation of a classic 2D softbody (blob) for the physics simulation.

from ..core.particle import Particle
from ..core.spring import Spring
from ..core.vector2d import Vector2D


class SoftBody:
    """
    A class representing a classic 2D softbody (blob) in the simulation.
    The softbody is composed of particles connected by springs in a hexagonal or triangular grid.
    """

    def __init__(
        self,
        position,
        width,
        height,
        rows,
        cols,
        particle_mass=1.0,
        spring_stiffness=1.0,
        spring_damping=0.1,
    ):
        """
        Initialize the softbody with a position, dimensions, grid resolution, and spring properties.

        Args:
            position (Vector2D): The initial position of the softbody.
            width (float): The width of the softbody.
            height (float): The height of the softbody.
            rows (int): The number of rows in the particle grid.
            cols (int): The number of columns in the particle grid.
            particle_mass (float, optional): The mass of each particle. Defaults to 1.0.
            spring_stiffness (float, optional): The stiffness of the springs. Defaults to 1.0.
            spring_damping (float, optional): The damping factor of the springs. Defaults to 0.1.
        """
        self.particles = []
        self.springs = []
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols

        # Calculate the spacing between particles
        self.spacing_x = width / (cols - 1) if cols > 1 else width
        self.spacing_y = height / (rows - 1) if rows > 1 else height

        # Create particles in a grid
        for row in range(rows):
            for col in range(cols):
                x = position.x + col * self.spacing_x
                y = position.y + row * self.spacing_y
                particle = Particle(Vector2D(x, y), particle_mass)
                self.particles.append(particle)

        # Create springs between particles
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col

                # Connect to the right neighbor
                if col < cols - 1:
                    right_index = index + 1
                    rest_length = self.spacing_x
                    spring = Spring(
                        self.particles[index],
                        self.particles[right_index],
                        rest_length,
                        spring_stiffness,
                        spring_damping,
                    )
                    self.springs.append(spring)

                # Connect to the bottom neighbor
                if row < rows - 1:
                    bottom_index = index + cols
                    rest_length = self.spacing_y
                    spring = Spring(
                        self.particles[index],
                        self.particles[bottom_index],
                        rest_length,
                        spring_stiffness,
                        spring_damping,
                    )
                    self.springs.append(spring)

                # Connect to the bottom-right neighbor (diagonal)
                # if row < rows - 1 and col < cols - 1:
                #     bottom_right_index = index + cols + 1
                #     rest_length = (self.spacing_x**2 + self.spacing_y**2) ** 0.5
                #     spring = Spring(
                #         self.particles[index],
                #         self.particles[bottom_right_index],
                #         rest_length,
                #         spring_stiffness,
                #         spring_damping,
                #     )
                #     self.springs.append(spring)

                # Connect to the bottom-left neighbor (diagonal)
                # if row < rows - 1 and col > 0:
                #     bottom_left_index = index + cols - 1
                #     rest_length = (self.spacing_x**2 + self.spacing_y**2) ** 0.5
                #     spring = Spring(
                #         self.particles[index],
                #         self.particles[bottom_left_index],
                #         rest_length,
                #         spring_stiffness,
                #         spring_damping,
                #     )
                #     self.springs.append(spring)

    def apply_force(self, force):
        """
        Apply a force to all particles in the softbody.

        Args:
            force (Vector2D): The force to apply.
        """
        for particle in self.particles:
            particle.apply_force(force)

    def update(self, delta_time):
        """
        Update the softbody by updating all particles and applying spring forces.

        Args:
            delta_time (float): The time step for the update.
        """
        # Apply external forces (e.g., gravity)
        for particle in self.particles:
            if not particle.is_fixed:
                particle.apply_force(Vector2D(0, 9.81))  # Apply gravity

        for spring in self.springs:
            spring.apply()

        for particle in self.particles:
            particle.update_position(delta_time)

    def render(self, renderer):
        """
        Render the softbody using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the softbody.
        """
        for spring in self.springs:
            renderer.draw_line(spring.particle1.position, spring.particle2.position)

        for particle in self.particles:
            renderer.draw_point(particle.position)

    def __repr__(self):
        return f"SoftBody(particles={len(self.particles)}, springs={len(self.springs)})"
