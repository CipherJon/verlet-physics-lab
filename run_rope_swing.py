import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from scenes.rope_swing import RopeSwingScene

if __name__ == "__main__":
    scene = RopeSwingScene()
    scene.run()
