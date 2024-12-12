import pygame
import random


# Balloon class
class Balloon:
    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = 20

    def move(self):
        """Move the balloon down."""
        self.y += self.speed

    def draw(self, screen):
        """Draw the balloon on the screen."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        """Check if the balloon is clicked."""
        return (self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2 <= self.radius ** 2