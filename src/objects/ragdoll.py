# ragdoll.py
# Implementation of a humanoid-like ragdoll for the physics simulation.

from core.particle import Particle
from core.spring import Spring
from core.vector2d import Vector2D


class Ragdoll:
    """
    A class representing a humanoid-like ragdoll with limbs.
    The ragdoll consists of multiple particles connected by springs to simulate joints and limbs.
    """

    def __init__(self, position, limb_length=20.0, stiffness=0.5, damping=0.1):
        """
        Initialize the ragdoll with a starting position, limb length, stiffness, and damping.

        Args:
            position (Vector2D): The starting position of the ragdoll.
            limb_length (float, optional): The length of each limb. Defaults to 20.0.
            stiffness (float, optional): The stiffness of the springs connecting the limbs. Defaults to 0.5.
            damping (float, optional): The damping factor for the springs. Defaults to 0.1.

        Raises:
            ValueError: If limb_length is not positive.
        """
        if limb_length <= 0:
            raise ValueError("Limb length must be positive.")
        self.limb_length = limb_length
        self.stiffness = stiffness
        self.damping = damping

        # Create particles for the ragdoll
        self.head = Particle(position, mass=5.0)
        self.torso = Particle(position + Vector2D(0, limb_length), mass=10.0)
        self.left_arm = Particle(
            position + Vector2D(-limb_length, limb_length * 1.5), mass=3.0
        )
        self.right_arm = Particle(
            position + Vector2D(limb_length, limb_length * 1.5), mass=3.0
        )
        self.left_leg = Particle(
            position + Vector2D(-limb_length * 0.5, limb_length * 2.5), mass=5.0
        )
        self.right_leg = Particle(
            position + Vector2D(limb_length * 0.5, limb_length * 2.5), mass=5.0
        )

        # Create springs to connect the particles
        self.springs = [
            Spring(
                self.head, self.torso, limb_length, stiffness, damping
            ),  # Head to torso
            Spring(
                self.torso, self.left_arm, limb_length, stiffness, damping
            ),  # Torso to left arm
            Spring(
                self.torso, self.right_arm, limb_length, stiffness, damping
            ),  # Torso to right arm
            Spring(
                self.torso, self.left_leg, limb_length, stiffness, damping
            ),  # Torso to left leg
            Spring(
                self.torso, self.right_leg, limb_length, stiffness, damping
            ),  # Torso to right leg
        ]

        # List of all particles in the ragdoll
        self.particles = [
            self.head,
            self.torso,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg,
        ]

    def apply_forces(self):
        """
        Apply forces to the ragdoll, such as gravity or external forces.
        """
        for particle in self.particles:
            particle.apply_force(Vector2D(0, 9.81))  # Apply gravity

    def update(self, delta_time):
        """
        Update the ragdoll's state for a given time step.

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
        Render the ragdoll using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the ragdoll.
        """
        for spring in self.springs:
            renderer.draw_line(spring.particle1.position, spring.particle2.position)

        for particle in self.particles:
            renderer.draw_point(particle.position, radius=5)

    def __repr__(self):
        return f"Ragdoll(particles={len(self.particles)}, springs={len(self.springs)})"
