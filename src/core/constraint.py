# constraint.py
# Base class for constraints in the softbody ragdoll simulation.


class Constraint:
    """
    Base class for all constraints in the simulation.
    Constraints define relationships between particles, such as distance, angle, or stiffness.
    """

    def __init__(self, particle1, particle2, rest_length):
        """
        Initialize the constraint with two particles and a rest length.

        Args:
            particle1 (Particle): The first particle.
            particle2 (Particle): The second particle.
            rest_length (float): The rest length of the constraint.
        """
        self.particle1 = particle1
        self.particle2 = particle2
        self.rest_length = rest_length

    def apply(self):
        """
        Apply the constraint to the particles.
        This method should be overridden by subclasses to implement specific constraint logic.
        """
        raise NotImplementedError("Subclasses must implement the apply method.")

    def satisfy(self):
        """
        Satisfy the constraint by adjusting the positions of the particles.
        """
        # Calculate the current distance between the particles
        current_distance = (
            self.particle1.position - self.particle2.position
        ).magnitude()

        # If the distance is not equal to the rest length, adjust the positions
        if current_distance != self.rest_length and current_distance != 0:
            # Calculate the displacement vector
            displacement = self.particle1.position - self.particle2.position
            direction = displacement.normalize()

            # Calculate the correction factor
            correction = (current_distance - self.rest_length) / 2

            # Adjust the positions of the particles
            self.particle1.position -= direction * correction
            self.particle2.position += direction * correction

    def render(self, renderer):
        """
        Render the constraint using the provided renderer.
        This method should be overridden by subclasses to implement specific rendering logic.
        """
        raise NotImplementedError("Subclasses must implement the render method.")
