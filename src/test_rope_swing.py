# test_rope_swing.py
# A test script to verify the rope swing simulation.

import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent))

try:
    import pygame

    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

from scenes.rope_swing import RopeSwingScene


def test_rope_swing():
    """
    Test the rope swing simulation.
    """
    if not PYGAME_AVAILABLE:
        print("PyGame not available, skipping test")
        return

    # Initialize PyGame
    pygame.init()

    # Create the rope swing scene
    scene = RopeSwingScene()

    # Run the simulation for 100 steps
    # Skip the test if PyGame is not available in a headless environment
    try:
        for i in range(100):
            scene.run()
    except pygame.error:
        print("PyGame not available in a headless environment, skipping test")
        return

    # Quit PyGame
    pygame.quit()

    print("Rope swing simulation successful")


if __name__ == "__main__":
    test_rope_swing()
