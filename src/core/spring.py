# spring.py
# Implementation of a spring constraint using position-based dynamics (PBD).


class Spring:
    """
    A class representing a spring (distance constraint) between two particles using position-based dynamics.
    This implementation uses direct position correction instead of force-based approaches.

    Attributes:
        particle1 (Particle): The first particle connected by the spring.
        particle2 (Particle): The second particle connected by the spring.
        rest_length (float): The rest length of the spring.
        stiffness (float): The stiffness of the spring (0-1 range, where 1 means full correction).
    """

    def __init__(self, particle1, particle2, rest_length, stiffness=1.0, damping=0.1):
        """
        Initialize the spring with two particles, rest length, stiffness, and damping.

        Args:
            particle1 (Particle): The first particle.
            particle2 (Particle): The second particle.
            rest_length (float): The rest length of the spring.
            stiffness (float, optional): The stiffness of the spring (0-1). Defaults to 1.0.
            damping (float, optional): The damping factor of the spring. Defaults to 0.1.

        Raises:
            ValueError: If stiffness is negative, rest_length is negative, or damping is negative.
        """
        if stiffness < 0 or stiffness > 1:
            raise ValueError("Stiffness must be between 0 and 1.")
        if rest_length < 0:
            raise ValueError("Rest length cannot be negative.")
        if damping < 0:
            raise ValueError("Damping cannot be negative.")
        self.particle1 = particle1
        self.particle2 = particle2
        self.rest_length = rest_length
        self.stiffness = stiffness
        self.damping = damping

    def apply(self):
        """
        Apply position-based correction to maintain the rest length of the spring.
        This uses the classic PBD approach for distance constraints.
        """
        # Calculate the current distance vector between particles
        delta = self.particle2.position - self.particle1.position
        current_length = delta.magnitude()

        # Avoid division by zero and skip if length is already correct
        if current_length == 0 or abs(current_length - self.rest_length) < 1e-6:
            return

        # Calculate the correction factor
        correction_factor = (current_length - self.rest_length) / current_length
        correction_vector = delta * correction_factor * 0.5 * self.stiffness

        # Apply correction based on inverse mass (if particles are not fixed)
        if not self.particle1.is_fixed:
            self.particle1.position += correction_vector * self.particle1.inv_mass
        if not self.particle2.is_fixed:
            self.particle2.position -= correction_vector * self.particle2.inv_mass

        # Apply damping to reduce oscillations
        velocity1 = self.particle1.position - self.particle1.old_position
        velocity2 = self.particle2.position - self.particle2.old_position
        relative_velocity = velocity2 - velocity1
        damping_force = relative_velocity * -self.damping

        if not self.particle1.is_fixed:
            self.particle1.acceleration += damping_force * self.particle1.inv_mass
        if not self.particle2.is_fixed:
            self.particle2.acceleration -= damping_force * self.particle2.inv_mass
