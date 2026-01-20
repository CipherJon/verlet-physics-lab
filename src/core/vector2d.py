class Vector2D:
    """
    A simple 2D vector class for handling vector operations in the physics simulation.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        # Type checking to prevent nested Vector2D objects
        if isinstance(x, Vector2D):
            raise TypeError(f"x cannot be a Vector2D object. Got: {x}")
        if isinstance(y, Vector2D):
            raise TypeError(f"y cannot be a Vector2D object. Got: {y}")
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numeric values.")
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors or a vector and a scalar."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2D(self.x + other, self.y + other)
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: 'Vector2D' and '{}'".format(
                    type(other).__name__
                )
            )

    def __radd__(self, other):
        """Add a scalar to a vector (reverse addition)."""
        if isinstance(other, (int, float)):
            return Vector2D(other + self.x, other + self.y)
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: '{}' and 'Vector2D'".format(
                    type(other).__name__
                )
            )

    def __sub__(self, other):
        """Subtract two vectors or a vector and a scalar."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return Vector2D(self.x - other, self.y - other)

    def __rsub__(self, other):
        """Subtract a vector from a scalar (reverse subtraction)."""
        if isinstance(other, (int, float)):
            return Vector2D(other - self.x, other - self.y)
        else:
            raise TypeError(
                "Unsupported operand type(s) for -: '{}' and 'Vector2D'".format(
                    type(other).__name__
                )
            )

    def __mul__(self, other):
        """Multiply a vector by a scalar."""
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError("Multiplication is only supported with scalars.")

    def __truediv__(self, other):
        """Divide a vector by a scalar."""
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        else:
            raise TypeError("Division is only supported with scalars.")

    def __neg__(self):
        """Negate the vector."""
        return Vector2D(-self.x, -self.y)

    def magnitude(self) -> float:
        """Calculate the magnitude (length) of the vector."""
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        """Normalize the vector to have a magnitude of 1."""
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector.")
        return Vector2D(self.x / mag, self.y / mag)

    def dot(self, other) -> float:
        """Calculate the dot product of two vectors."""
        return self.x * other.x + self.y * other.y

    def copy(self):
        """Return a copy of the vector."""
        return Vector2D(self.x, self.y)

    def distance_to(self, other):
        """Calculate the distance between this vector and another vector."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __eq__(self, other):
        """Check if two vectors are equal."""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
