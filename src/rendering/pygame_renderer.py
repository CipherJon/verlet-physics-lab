# pygame_renderer.py
# Implementation of a Pygame-based renderer for the physics simulation.

import pygame

from core.vector2d import Vector2D


class PygameRenderer:
    """
    A renderer for visualizing the physics simulation using Pygame.
    This renderer provides methods for drawing particles, springs, and other simulation elements.
    """

    def __init__(self, width=800, height=600, background_color=(0, 0, 0)):
        """
        Initialize the Pygame renderer with a window size and background color.

        Args:
            width (int, optional): The width of the Pygame window. Defaults to 800.
            height (int, optional): The height of the Pygame window. Defaults to 600.
            background_color (tuple, optional): The background color of the window as an RGB tuple. Defaults to (0, 0, 0).
        """
        pygame.init()
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Softbody Ragdoll Simulation")
        self.clock = pygame.time.Clock()
        self.running = False

    def start(self):
        """
        Start the Pygame renderer and enter the main loop.
        """
        self.running = True
        while self.running:
            self._handle_events()
            self._clear_screen()
            self._render_frame()
            pygame.display.flip()
            self.clock.tick(60)  # Cap the frame rate at 60 FPS

    def stop(self):
        """
        Stop the Pygame renderer and exit the main loop.
        """
        self.running = False

    def _handle_events(self):
        """
        Handle Pygame events, such as quitting the application.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _clear_screen(self):
        """
        Clear the screen with the background color.
        """
        self.screen.fill(self.background_color)

    def _render_frame(self):
        """
        Render a single frame of the simulation.
        This method should be overridden by subclasses to implement custom rendering logic.
        """
        pass

    def draw_point(self, position, color=(255, 255, 255), radius=3):
        """
        Draw a point (circle) at the specified position.

        Args:
            position (Vector2D): The position of the point.
            color (tuple, optional): The color of the point as an RGB tuple. Defaults to (255, 255, 255).
            radius (int, optional): The radius of the point. Defaults to 3.
        """
        pygame.draw.circle(
            self.screen,
            color,
            (int(position.x), int(position.y)),
            radius,
        )

    def draw_line(self, start, end, color=(255, 255, 255), width=1):
        """
        Draw a line between two points.

        Args:
            start (Vector2D): The starting position of the line.
            end (Vector2D): The ending position of the line.
            color (tuple, optional): The color of the line as an RGB tuple. Defaults to (255, 255, 255).
            width (int, optional): The width of the line. Defaults to 1.
        """
        pygame.draw.line(
            self.screen,
            color,
            (int(start.x), int(start.y)),
            (int(end.x), int(end.y)),
            width,
        )

    def draw_spring(self, spring, color=(255, 255, 255), width=1):
        """
        Draw a spring between two particles.

        Args:
            spring (Spring): The spring to draw.
            color (tuple, optional): The color of the spring as an RGB tuple. Defaults to (255, 255, 255).
            width (int, optional): The width of the spring. Defaults to 1.
        """
        self.draw_line(
            spring.particle1.position, spring.particle2.position, color, width
        )

    def draw_particle(self, particle, color=(255, 255, 255), radius=3):
        """
        Draw a particle at its current position.

        Args:
            particle (Particle): The particle to draw.
            color (tuple, optional): The color of the particle as an RGB tuple. Defaults to (255, 255, 255).
            radius (int, optional): The radius of the particle. Defaults to 3.
        """
        self.draw_point(particle.position, color, radius)

    def __del__(self):
        """
        Clean up Pygame resources when the renderer is destroyed.
        """
        pygame.quit()
