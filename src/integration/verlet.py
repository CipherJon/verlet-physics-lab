# verlet.py
# Implementation of the Verlet integration method for the physics simulation.
# Updated to use position-based dynamics with multiple constraint iterations.

from src.core.vector2d import Vector2D


class VerletIntegrator:
    """
    A class for performing Verlet integration on particles in the simulation.
    Verlet integration is a numerical method for integrating equations of motion.
    It is particularly useful for simulating systems with constraints.

    This implementation uses position-based dynamics (PBD) with multiple constraint iterations
    for stable, realistic simulations.

    Attributes:
        particles (list[Particle]): A list of particles to integrate.
        constraints (list[Constraint]): A list of constraints to apply.
        constraint_iterations (int): Number of constraint iterations per time step.
        damping (float): Global damping factor (0-1) to reduce oscillations.
        gravity (Vector2D): Gravity acceleration vector.
    """

    def __init__(
        self,
        particles,
        constraints=None,
        constraint_iterations=8,
        damping=0.99,
        gravity=None,
    ):
        """
        Initialize the Verlet integrator with a list of particles and optional constraints.

        Args:
            particles (list[Particle]): A list of particles to integrate.
            constraints (list[Constraint], optional): A list of constraints to apply. Defaults to None.
            constraint_iterations (int, optional): Number of constraint iterations. Defaults to 8.
            damping (float, optional): Global damping factor (0-1). Defaults to 0.99.
            gravity (Vector2D, optional): Gravity acceleration vector. Defaults to None.
        """
        self.particles = particles
        self.constraints = constraints if constraints is not None else []
        self.constraint_iterations = constraint_iterations
        self.damping = damping
        self.gravity = gravity if gravity is not None else Vector2D(0, 0)

    def integrate(self, delta_time):
        """
        Perform Verlet integration for one time step using position-based dynamics.

        Args:
            delta_time (float): The time step for the integration.
        """
        # Step 1: Apply gravity as acceleration to non-fixed particles
        for particle in self.particles:
            if not particle.is_fixed:
                particle.acceleration += self.gravity

        # Step 2: Verlet integration - update positions based on current acceleration
        for particle in self.particles:
            if not particle.is_fixed:
                # Calculate velocity from the current and old positions
                velocity = particle.position - particle.old_position

                # Store the current position as the old position
                particle.old_position = particle.position.copy()

                # Update the position using the velocity and acceleration
                particle.position += velocity + particle.acceleration * (delta_time**2)

                # Reset acceleration for the next time step
                particle.acceleration = Vector2D(0, 0)

        # Step 3: Apply constraints multiple times for stability
        for _ in range(self.constraint_iterations):
            for constraint in self.constraints:
                constraint.apply()

        # Step 4: Apply global damping to reduce oscillations
        if self.damping > 0 and self.damping < 1:
            for particle in self.particles:
                if not particle.is_fixed:
                    velocity = particle.position - particle.old_position
                    particle.position = particle.old_position + velocity * self.damping

    def apply_force(self, particle_index, force):
        """
        Apply a force to a specific particle.

        Args:
            particle_index (int): The index of the particle to apply the force to.
            force (Vector2D): The force to apply.
        """
        if 0 <= particle_index < len(self.particles):
            self.particles[particle_index].apply_force(force)
        else:
            raise IndexError("Particle index out of range.")
