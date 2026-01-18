# Issues in Verlet Physics Lab

## ModuleNotFoundError: No module named 'core'

### Description
Multiple test files are failing due to the `ModuleNotFoundError: No module named 'core'`. This error occurs when Python cannot locate the `core` module, which contains essential classes like `Vector2D`, `Particle`, and others.

### Affected Files
1. `src/scenes/stress_test.py`
2. `src/test_integration.py`
3. `src/test_rendering.py`
4. `src/test_rope_swing.py`
5. `src/test_simulation.py`
6. `tests/integration/test_cloth.py`
7. `tests/integration/test_ragdoll.py`
8. `tests/integration/test_rope.py`
9. `tests/integration/test_softbody.py`

### Root Cause
The `core` module is not being recognized as a valid Python module. This could be due to:
- Incorrect Python path configuration.
- Missing `__init__.py` files in the `core` directory.
- Incorrect import statements in the affected files.

### Steps to Reproduce
1. Run the test files using `pytest` or `python3`.
2. Observe the `ModuleNotFoundError: No module named 'core'` error.

### Solution
1. Ensure that the `core` directory contains an `__init__.py` file.
2. Verify that the Python path includes the `src` directory.
3. Update import statements to use the correct module path (e.g., `from src.core.vector2d import Vector2D`).

### Additional Notes
- The `core` directory already contains an `__init__.py` file, so the issue might be related to the Python path or import statements.
- The `src` directory is a Python package, so imports should be relative to the `src` directory.

## Simulation Killed During Execution

### Description
The `RopeSwingScene` simulation is being killed during execution. This issue occurs when running the simulation with the `DebugRenderer`.

### Affected Files
1. `src/scenes/rope_swing.py`

### Root Cause
The simulation is being killed, likely due to:
- Resource constraints (e.g., memory or CPU usage).
- An infinite loop or excessive computation in the simulation loop.
- Issues with the `DebugRenderer` or PyGame.

### Steps to Reproduce
1. Run the `RopeSwingScene` using `python3 test_rope_swing.py`.
2. Observe that the script is killed during execution.

### Solution
1. Reduce the number of particles in the rope.
2. Use a smaller time step for the simulation.
3. Reduce the gravity force applied to the particles.
4. Debug the `DebugRenderer` to identify any issues with rendering.

### Additional Notes
- The simulation works correctly without rendering.
- The issue might be related to the environment or the way the simulation is being run.

## Next Steps
1. Fix the `ModuleNotFoundError` by updating import statements and ensuring the Python path is correct.
2. Debug the `RopeSwingScene` to identify the cause of the simulation being killed.
3. Test the fixes to ensure that the simulation runs correctly.