# stress_test.py
# A scene for stress-testing the physics simulation with a large number of objects.

from ..core.vector2d import Vector2D
from ..objects.cloth import Cloth
from ..objects.ragdoll import Ragdoll
from ..objects.rope import Rope
from ..objects.softbody import SoftBody


class StressTestScene:
    """
    A scene designed to stress-test the physics simulation by creating a large number of objects.
    This scene includes multiple ropes, ragdolls, softbodies, and cloths to test performance and stability.
    """

    def __init__(self):
        """
        Initialize the stress test scene with multiple objects.
        """
        self.ropes = []
        self.ragdolls = []
        self.softbodies = []
        self.cloths = []

        # Create multiple ropes
        for i in range(5):
            start_position = Vector2D(100 + i * 50, 50)
            rope = Rope(start_position, num_particles=20, segment_length=5.0)
            self.ropes.append(rope)

        # Create multiple ragdolls
        for i in range(3):
            position = Vector2D(300 + i * 100, 100)
            ragdoll = Ragdoll(position, limb_length=20.0)
            self.ragdolls.append(ragdoll)

        # Create multiple softbodies
        for i in range(4):
            position = Vector2D(500 + i * 80, 150)
            softbody = SoftBody(position, width=30, height=30, rows=5, cols=5)
            self.softbodies.append(softbody)

        # Create multiple cloths
        for i in range(2):
            position = Vector2D(200 + i * 200, 200)
            cloth = Cloth(width=10, height=10)
            self.cloths.append(cloth)

    def update(self, delta_time):
        """
        Update all objects in the stress test scene.

        Args:
            delta_time (float): The time step for the update.
        """
        for rope in self.ropes:
            rope.update(delta_time)

        for ragdoll in self.ragdolls:
            ragdoll.update(delta_time)

        for softbody in self.softbodies:
            softbody.update(delta_time)

        for cloth in self.cloths:
            cloth.update(delta_time)

    def render(self, renderer):
        """
        Render all objects in the stress test scene using the provided renderer.

        Args:
            renderer: The renderer to use for drawing the objects.
        """
        for rope in self.ropes:
            rope.render(renderer)

        for ragdoll in self.ragdolls:
            ragdoll.render(renderer)

        for softbody in self.softbodies:
            softbody.render(renderer)

        for cloth in self.cloths:
            cloth.render(renderer)

    def __repr__(self):
        return f"StressTestScene(ropes={len(self.ropes)}, ragdolls={len(self.ragdolls)}, softbodies={len(self.softbodies)}, cloths={len(self.cloths)})"
