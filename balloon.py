import pygame
import random
import balloon_class

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

screen = pygame.display .set_mode(400,600)
pygame.display.set_caption("Balloon Game")


def event1(Balloons,score):
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            return False,score
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for balloon in Balloons[:]:
                if balloon.is_clicked(pos):
                    Balloons.remove(balloon)
                    score += 1
    return True, score


def event2


