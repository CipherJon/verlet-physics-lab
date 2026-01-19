# Issues in Verlet Physics Lab

## Test Failures

### Description
Two tests are failing due to issues with the `Vector2D` class and its operations.

### Affected Files
1. `tests/integration/test_ragdoll.py::TestRagdoll::test_update`
2. `tests/integration/test_softbody.py::TestSoftBody::test_apply_force`

### Root Cause
1. `TypeError: unsupported operand type(s) for ** or pow(): 'Vector2D' and 'int'`: This error suggests that the `Vector2D` class does not support exponentiation operations with integers.
2. `AssertionError: Vector2D(Vector2D(0.0, 9.81), Vector2D(0.0, 9.81)) != Vector2D(0, 9.81)`: This error indicates a mismatch in the expected and actual values of a `Vector2D` object, possibly due to incorrect initialization or comparison logic.

### Steps to Reproduce
1. Run the failing tests using `pytest`.
2. Observe the errors related to `Vector2D` operations.
