# matplotlib_renderer.py
# Implementation of a renderer using Matplotlib for analysis and plotting.

import matplotlib.pyplot as plt
import numpy as np

class MatplotlibRenderer:
    """
    A renderer for visualizing the physics simulation using Matplotlib.
    This renderer is useful for analysis and plotting trajectories.
    """

    def __init__(self):
        """
        Initialize the Matplotlib renderer.
        """
        self.fig, self.ax = plt.subplots()
        self.lines = []
        self.points = []

    def draw_line(self, start, end, color='b'):
        """
        Draw a line between two points.

        Args:
            start (Vector2D): The starting point of the line.
            end (Vector2D): The ending point of the line.
            color (str, optional): The color of the line. Defaults to 'b' (blue).
        """
        line, = self.ax.plot([start.x, end.x], [start.y, end.y], color=color)
        self.lines.append(line)

    def draw_point(self, position, color='r', radius=2):
        """
        Draw a point at a given position.

        Args:
            position (Vector2D): The position of the point.
            color (str, optional): The color of the point. Defaults to 'r' (red).
            radius (int, optional): The radius of the point. Defaults to 2.
        """
        point, = self.ax.plot(position.x, position.y, 'o', color=color, markersize=radius)
        self.points.append(point)

    def clear(self):
        """
        Clear the current plot.
        """
        for line in self.lines:
            line.remove()
        for point in self.points:
            point.remove()
        self.lines = []
        self.points = []

    def update(self):
        """
        Update the plot to reflect the current state.
        """
        plt.draw()
        plt.pause(0.01)

    def close(self):
        """
        Close the plot window.
        """
        plt.close(self.fig)

    def __repr__(self):
        return "MatplotlibRenderer()"
```

Now, let's create the `debug_renderer.py` file.
