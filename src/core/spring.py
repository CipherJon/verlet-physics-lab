class Spring:
    """
    A class representing a spring (distance constraint) between two particles.

    Attributes:
        particle1 (Particle): The first particle connected by the spring.
        particle2 (Particle): The second particle connected by the spring.
        rest_length (float): The rest length of the spring.
        stiffness (float): The stiffness of the spring.
        damping (float): The damping factor of the spring.
    """

    def __init__(self, particle1, particle2, rest_length, stiffness=1.0, damping=0.1):
        """
        Initialize the spring with two particles, rest length, stiffness, and damping.

        Args:
            particle1 (Particle): The first particle.
            particle2 (Particle): The second particle.
            rest_length (float): The rest length of the spring.
            stiffness (float, optional): The stiffness of the spring. Defaults to 1.0.
            damping (float, optional): The damping factor of the spring. Defaults to 0.1.
        """
        self.particle1 = particle1
        self.particle2 = particle2
        self.rest_length = rest_length
        self.stiffness = stiffness
        self.damping = damping

    def apply(self):
        """
        Apply the spring force to the connected particles.
        """
        # Calculate the current distance between the particles
        current_distance = (
            self.particle1.position - self.particle2.position
        ).magnitude()

        # Calculate the displacement vector
        displacement = self.particle1.position - self.particle2.position
        direction = displacement.normalize()

        # Calculate the force magnitude using Hooke's Law
        force_magnitude = self.stiffness * (current_distance - self.rest_length)

        # Apply the force to both particles
        force = direction * force_magnitude
        self.particle1.apply_force(force)
        self.particle2.apply_force(-force)

        # Apply damping (optional)
        if self.damping > 0:
            # Calculate relative velocity
            relative_velocity = self.particle1.velocity - self.particle2.velocity
            damping_force = (
                direction * (relative_velocity.dot(direction)) * self.damping
            )
            self.particle1.apply_force(-damping_force)
            self.particle2.apply_force(damping_force)
