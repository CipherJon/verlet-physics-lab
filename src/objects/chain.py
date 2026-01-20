# chain.py
# Implementation of the Chain class for simulating a chain with angle constraints.

from ..core.constraint import Constraint
from ..core.particle import Particle
from ..core.spring import Spring
from ..core.vector2d import Vector2D


class Chain:
    """
    A class representing a chain with angle constraints.
    A chain is a series of particles connected by springs, with additional angle constraints to maintain rigidity.
    """

    def __init__(
        self,
        num_links=None,
        particle_count=None,
        link_length=1.0,
        position=None,
        stiffness=1.0,
        damping=0.1,
        particle_mass=1.0,
        spring_stiffness=None,
        spring_damping=None,
    ):
        """
        Initialize the chain with a number of links, link length, starting position, stiffness, and damping.

        Args:
            num_links (int, optional): The number of links in the chain. Defaults to None.
            particle_count (int, optional): The number of particles in the chain. Defaults to None.
            link_length (float, optional): The length of each link. Defaults to 1.0.
            position (Vector2D, optional): The starting position of the chain. Defaults to None.
            stiffness (float, optional): The stiffness of the springs. Defaults to 1.0.
            damping (float, optional): The damping factor of the springs. Defaults to 0.1.
            particle_mass (float, optional): The mass of each particle. Defaults to 1.0.
        """
        self.num_links = num_links if num_links is not None else particle_count
        if self.num_links is None:
            raise ValueError("Either num_links or particle_count must be provided.")
        if self.num_links <= 0:
            raise ValueError("Number of links must be positive.")
        self.link_length = link_length
        self.stiffness = spring_stiffness if spring_stiffness is not None else stiffness
        self.damping = spring_damping if spring_damping is not None else damping
        self.particle_mass = particle_mass
        self.particles = []
        self.springs = []
        self.constraints = []

        # Create particles and springs for the chain
        for i in range(self.num_links):
            # Create a particle for each link
            particle_position = Vector2D(i * link_length, 0)
            if position is not None:
                particle_position += position
            particle = Particle(particle_position, mass=particle_mass)
            self.particles.append(particle)

            # Create a spring between consecutive particles
            if i > 0:
                spring = Spring(
                    self.particles[i - 1],
                    self.particles[i],
                    link_length,
                    self.stiffness,
                    self.damping,
                )
                self.springs.append(spring)

        # Fix the first particle to create an anchor point
        if self.particles:
            self.particles[0].is_fixed = True

    def add_angle_constraint(
        self, particle1_index, particle2_index, particle3_index, angle
    ):
        """
        Add an angle constraint between three particles to maintain a specific angle.

        Args:
            particle1_index (int): Index of the first particle.
            particle2_index (int): Index of the second particle (vertex of the angle).
            particle3_index (int): Index of the third particle.
            angle (float): The desired angle in radians.
        """
        if (
            0 <= particle1_index < len(self.particles)
            and 0 <= particle2_index < len(self.particles)
            and 0 <= particle3_index < len(self.particles)
        ):
            constraint = AngleConstraint(
                self.particles[particle1_index],
                self.particles[particle2_index],
                self.particles[particle3_index],
                angle,
            )
            self.constraints.append(constraint)
        else:
            raise IndexError("Particle index out of range.")

    def update(self, delta_time):
        """
        Update the chain by applying forces and constraints.

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

        # Apply angle constraints
        for constraint in self.constraints:
            constraint.apply()

        # Update particle positions
        for particle in self.particles:
            particle.update_position(delta_time)

    def render(self, renderer):
        """
        Render the chain using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the chain.
        """
        for spring in self.springs:
            renderer.draw_spring(spring)

        for particle in self.particles:
            renderer.draw_particle(particle)


class AngleConstraint(Constraint):
    """
    A constraint to maintain a specific angle between three particles.
    """

    def __init__(self, particle1, particle2, particle3, angle):
        """
        Initialize the angle constraint with three particles and a desired angle.

        Args:
            particle1 (Particle): The first particle.
            particle2 (Particle): The second particle (vertex of the angle).
            particle3 (Particle): The third particle.
            angle (float): The desired angle in radians.
        """
        super().__init__()
        self.particle1 = particle1
        self.particle2 = particle2
        self.particle3 = particle3
        self.angle = angle

    def apply(self):
        """
        Apply the angle constraint to the particles.
        """
        # Calculate vectors from particle2 to particle1 and particle3
        v1 = self.particle1.position - self.particle2.position
        v2 = self.particle3.position - self.particle2.position

        # Calculate the current angle between the vectors
        current_angle = v1.angle_between(v2)

        # Calculate the angle difference
        angle_diff = current_angle - self.angle

        # Apply corrective forces to maintain the desired angle
        # This is a simplified approach; a more accurate method would involve torque and angular velocity
        force_magnitude = 0.1 * angle_diff  # Adjust the multiplier as needed

        # Calculate perpendicular vectors for applying torque
        perpendicular1 = v1.perpendicular().normalized()
        perpendicular2 = v2.perpendicular().normalized()

        # Apply forces to particle1 and particle3
        self.particle1.apply_force(perpendicular1 * force_magnitude)
        self.particle3.apply_force(perpendicular2 * force_magnitude)

    def render(self, renderer):
        """
        Render the angle constraint using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the constraint.
        """
        renderer.draw_line(self.particle1.position, self.particle2.position)
        renderer.draw_line(self.particle2.position, self.particle3.position)
