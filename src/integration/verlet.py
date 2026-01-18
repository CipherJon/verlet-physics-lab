# verlet.py
# Implementation of the Verlet integration method for the physics simulation.

from core.vector2d import Vector2D


class VerletIntegrator:
    """
    A class for performing Verlet integration on particles in the simulation.
    Verlet integration is a numerical method for integrating equations of motion.
    It is particularly useful for simulating systems with constraints.
    """

    def __init__(self, particles, constraints=None):
        """
        Initialize the Verlet integrator with a list of particles and optional constraints.

        Args:
            particles (list[Particle]): A list of particles to integrate.
            constraints (list[Constraint], optional): A list of constraints to apply. Defaults to None.
        """
        self.particles = particles
        self.constraints = constraints if constraints is not None else []

    def integrate(self, delta_time):
        """
        Perform Verlet integration for one time step.

        Args:
            delta_time (float): The time step for the integration.
        """
        # Update particle positions using Verlet integration
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

        # Apply constraints (if any)
        for constraint in self.constraints:
            constraint.apply()

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
