class EulerIntegrator:
    """
    A class for performing Euler integration on particles in the simulation.
    Euler integration is a simple method for numerical integration.
    """

    @staticmethod
    def update(particles, delta_time):
        """
        Update the positions of the particles using Euler integration.

        Args:
            particles (list[Particle]): A list of particles to update.
            delta_time (float): The time step for the update.
        """
        for particle in particles:
            if not particle.is_fixed:
                # Update velocity based on acceleration
                particle.velocity += particle.acceleration * delta_time

                # Update position based on velocity
                particle.position += particle.velocity * delta_time

                # Reset acceleration for the next time step
                particle.acceleration = Vector2D(0, 0)
