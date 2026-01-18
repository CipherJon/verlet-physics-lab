# cloth_flag.py
# Implementation of a cloth flag scene for the physics simulation.

from core.vector2d import Vector2D
from objects.cloth import Cloth
from scenes.scene_base import SceneBase


class ClothFlagScene(SceneBase):
    """
    A scene demonstrating a cloth flag simulation.
    The cloth is fixed at the top and allowed to sway in the wind.
    """

    def __init__(self):
        """
        Initialize the cloth flag scene.
        """
        super().__init__()
        self.cloth = None
        self.wind_force = Vector2D(0.5, 0)  # Constant wind force

    def setup(self):
        """
        Set up the cloth flag scene.
        """
        # Create a cloth with 10x10 particles
        self.cloth = Cloth(width=10, height=10)

        # Fix the top row of particles to simulate a flagpole
        for i in range(10):
            self.cloth.particles[i].is_fixed = True

    def update(self, delta_time):
        """
        Update the cloth flag scene for a given time step.

        Args:
            delta_time (float): The time step for the update.
        """
        # Apply wind force to the cloth
        for particle in self.cloth.particles:
            if not particle.is_fixed:
                particle.apply_force(self.wind_force)

        # Update the cloth
        self.cloth.update(delta_time)

    def render(self, renderer):
        """
        Render the cloth flag scene using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the scene.
        """
        # Render the cloth
        self.cloth.render(renderer)

    def __repr__(self):
        return "ClothFlagScene()"
