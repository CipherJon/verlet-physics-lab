class Particle:
    """
    A basic mass point in the simulation.

    Attributes:
        position (Vector2D): The current position of the particle.
        old_position (Vector2D): The previous position of the particle (used for Verlet integration).
        acceleration (Vector2D): The current acceleration of the particle.
        mass (float): The mass of the particle.
        inv_mass (float): The inverse mass of the particle (1/mass).
        is_fixed (bool): Whether the particle is fixed in space (e.g., anchored).
    """

    def __init__(self, position, mass=1.0, is_fixed=False):
        """
        Initialize a particle with a position, mass, and fixed status.

        Args:
            position (Vector2D): The initial position of the particle.
            mass (float): The mass of the particle. Defaults to 1.0.
            is_fixed (bool): Whether the particle is fixed in space. Defaults to False.
        """
        self.position = position
        self.old_position = position.copy()
        self.acceleration = Vector2D(0, 0)
        self.mass = mass
        self.inv_mass = 1.0 / mass if mass != 0 else 0.0
        self.is_fixed = is_fixed

    def apply_force(self, force):
        """
        Apply a force to the particle.

        Args:
            force (Vector2D): The force to apply.
        """
        if not self.is_fixed:
            self.acceleration += force * self.inv_mass

    def update_position(self, delta_time):
        """
        Update the particle's position using Euler integration.

        Args:
            delta_time (float): The time step for the update.
        """
        if not self.is_fixed:
            velocity = self.position - self.old_position
            self.old_position = self.position.copy()
            self.position += velocity + self.acceleration * (delta_time**2)
            self.acceleration = Vector2D(0, 0)

    def __repr__(self):
        return f"Particle(position={self.position}, mass={self.mass}, is_fixed={self.is_fixed})"
