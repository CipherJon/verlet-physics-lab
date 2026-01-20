# Issues in Verlet Physics Lab

## Current Issue

### Error: Unsupported operand type(s) for +: 'Vector2D' and 'Vector2D'

**File:** `verlet-physics-lab/src/integration/verlet.py`

**Line:** `particle.acceleration += self.gravity`

**Description:**
The error occurs when trying to add the `gravity` attribute to the `acceleration` attribute of the `Particle` class. The `gravity` attribute is correctly defined as a `Vector2D` object and passed to the `VerletIntegrator`. However, the error suggests that the `gravity` attribute might not be a `Vector2D` object when the `integrate` method is called.

**Steps to Reproduce:**
1. Run the script using `python3 main.py`.
2. Select the "Rope Swing" scene.
3. The error occurs when the `integrate` method is called in the `VerletIntegrator` class.

**Possible Causes:**
1. The `gravity` attribute might not be a `Vector2D` object when the `integrate` method is called.
2. The `gravity` attribute might be modified or overwritten before the `integrate` method is called.
3. There might be an issue with the `Vector2D` class's `__add__` method.

**Next Steps:**
1. Add debug statements to check the type of the `gravity` attribute before the `integrate` method is called.
2. Verify that the `gravity` attribute is not being modified or overwritten before the `integrate` method is called.
3. Check the `Vector2D` class's `__add__` method to ensure it supports adding two `Vector2D` objects.

## Known Issues

### Issue: EOFError: EOF when reading a line

**File:** `verlet-physics-lab/main.py`

**Line:** `choice = input("Enter your choice (1-6): ")`

**Description:**
The error occurs when the script is waiting for user input, but no input is being provided. This is expected behavior for a script that prompts the user for input.
