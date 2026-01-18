# constraint.py
# Base class for constraints in the softbody ragdoll simulation.


class Constraint:
    """
    Base class for all constraints in the simulation.
    Constraints define relationships between particles, such as distance, angle, or stiffness.
    """

    def __init__(self):
        """
        Initialize the constraint.
        """
        pass

    def apply(self):
        """
        Apply the constraint to the particles.
        This method should be overridden by subclasses to implement specific constraint logic.
        """
        raise NotImplementedError("Subclasses must implement the apply method.")

    def render(self, renderer):
        """
        Render the constraint using the provided renderer.
        This method should be overridden by subclasses to implement specific rendering logic.
        """
        raise NotImplementedError("Subclasses must implement the render method.")
