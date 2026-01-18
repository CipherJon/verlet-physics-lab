# debug_renderer.py
# A simple renderer for debugging purposes, drawing lines and points.

import pygame

from core.vector2d import Vector2D


class DebugRenderer:
    """
    A simple renderer for debugging purposes.
    This renderer draws lines and points to visualize the simulation.
    """

    def __init__(self, width=800, height=600, background_color=(0, 0, 0)):
        """
        Initialize the debug renderer with a window size and background color.

        Args:
            width (int, optional): The width of the rendering window. Defaults to 800.
            height (int, optional): The height of the rendering window. Defaults to 600.
            background_color (tuple, optional): The background color of the window. Defaults to (0, 0, 0).
        """
        pygame.init()
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Debug Renderer")

    def draw_line(self, start, end, color=(255, 255, 255)):
        """
        Draw a line between two points.

        Args:
            start (Vector2D): The starting point of the line.
            end (Vector2D): The ending point of the line.
            color (tuple, optional): The color of the line. Defaults to (255, 255, 255).
        """
        pygame.draw.line(self.screen, color, (start.x, start.y), (end.x, end.y), 1)

    def draw_point(self, position, color=(255, 0, 0), radius=3):
        """
        Draw a point at a given position.

        Args:
            position (Vector2D): The position of the point.
            color (tuple, optional): The color of the point. Defaults to (255, 0, 0).
            radius (int, optional): The radius of the point. Defaults to 3.
        """
        pygame.draw.circle(
            self.screen, color, (int(position.x), int(position.y)), radius
        )

    def clear(self):
        """
        Clear the screen with the background color.
        """
        self.screen.fill(self.background_color)

    def render(self):
        """
        Update the display to show the rendered content.
        """
        pygame.display.flip()

    def handle_events(self):
        """
        Handle PyGame events, such as quitting the application.
        Returns True if the application should continue running, False otherwise.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def __del__(self):
        """
        Clean up PyGame resources when the renderer is destroyed.
        """
        pygame.quit()
