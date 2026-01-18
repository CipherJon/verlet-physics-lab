# blob_slime.py
# Implementation of the BlobSlime scene for demonstrating a slime-like softbody.

from core.vector2d import Vector2D
from objects.softbody import SoftBody


class BlobSlime:
    """
    A scene demonstrating a slime-like softbody.
    The softbody is initialized with specific properties to simulate a blob of slime.
    """

    def __init__(self):
        """
        Initialize the BlobSlime scene with a softbody.
        """
        # Create a softbody with specific properties for a slime-like behavior
        self.softbody = SoftBody(
            position=Vector2D(400, 300),
            width=100,
            height=100,
            rows=5,
            cols=5,
            particle_mass=1.0,
            spring_stiffness=0.5,
            spring_damping=0.2,
        )

    def update(self, delta_time):
        """
        Update the scene for a given time step.

        Args:
            delta_time (float): The time step for the update.
        """
        self.softbody.update(delta_time)

    def render(self, renderer):
        """
        Render the scene using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the scene.
        """
        self.softbody.render(renderer)

    def __repr__(self):
        return "BlobSlime()"
