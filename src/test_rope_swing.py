# test_rope_swing.py
# A test script to verify the RopeSwingScene.

from scenes.rope_swing import RopeSwingScene


def test_rope_swing():
    """
    Test the RopeSwingScene with a smaller number of particles.
    """
    # Create the scene with a smaller number of particles
    scene = RopeSwingScene(num_particles=3)

    # Run the scene
    scene.run()


if __name__ == "__main__":
    test_rope_swing()
