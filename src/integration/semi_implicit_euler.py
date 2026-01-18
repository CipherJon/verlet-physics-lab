class SemiImplicitEulerIntegrator:
    """
    Semi-Implicit Euler integration method for the physics simulation.
    This method is more stable than explicit Euler and is commonly used in physics simulations.
    """

    def __init__(self, particles, constraints, gravity=Vector2D(0, 9.81), damping=0.99):
        """
        Initialize the integrator with particles, constraints, gravity, and damping.

        Args:
            particles (list[Particle]): List of particles in the simulation.
            constraints (list[Constraint]): List of constraints in the simulation.
            gravity (Vector2D, optional): Gravity vector. Defaults to Vector2D(0, 9.81).
            damping (float, optional): Damping factor to reduce velocity over time. Defaults to 0.99.
        """
        self.particles = particles
        self.constraints = constraints
        self.gravity = gravity
        self.damping = damping

    def step(self, delta_time):
        """
        Perform a single integration step.

        Args:
            delta_time (float): The time step for the update.
        """
        # Apply gravity to all particles
        for particle in self.particles:
            if not particle.is_fixed:
                particle.apply_force(self.gravity * particle.mass)

        # Update particle positions using semi-implicit Euler
        for particle in self.particles:
            if not particle.is_fixed:
                # Update velocity
                particle.velocity += particle.acceleration * delta_time
                particle.velocity *= self.damping  # Apply damping

                # Update position
                particle.position += particle.velocity * delta_time

                # Reset acceleration
                particle.acceleration = Vector2D(0, 0)

        # Apply constraints
        for constraint in self.constraints:
            constraint.apply()

    def __repr__(self):
        return f"SemiImplicitEulerIntegrator(particles={len(self.particles)}, constraints={len(self.constraints)})"
