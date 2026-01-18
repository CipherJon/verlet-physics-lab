# main.py
# Entry point for the simple-softbody-ragdoll simulation.
# This script allows users to choose a scene and run the simulation.

from scenes.rope_swing import RopeSwingScene
from scenes.ragdoll_fall import RagdollFallScene
from scenes.blob_slime import BlobSlime
from scenes.cloth_flag import ClothFlagScene
from scenes.stress_test import StressTestScene

def main():
    """
    Main function to run the simulation.
    Prompts the user to choose a scene and runs the selected scene.
    """
    print("Simple Softbody Ragdoll Simulation")
    print("=================================")
    print("Choose a scene to run:")
    print("1. Rope Swing")
    print("2. Ragdoll Fall")
    print("3. Blob Slime")
    print("4. Cloth Flag")
    print("5. Stress Test")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            scene = RopeSwingScene()
            scene.run()
        elif choice == "2":
            scene = RagdollFallScene()
            scene.run()
        elif choice == "3":
            scene = BlobSlime()
            scene.run()
        elif choice == "4":
            scene = ClothFlagScene()
            scene.run()
        elif choice == "5":
            scene = StressTestScene()
            scene.run()
        elif choice == "6":
            print("Exiting the simulation.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```

Now, let's create the `requirements.txt` file to list the project's dependencies.{"display_description": "Create requirements.txt", "path": "verlet-physics-lab/simple-softbody-ragdoll/requirements.txt", "mode": "create"}
