import os
import pygame
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOUD = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()


    def update(self):
        self.x -= game_speed

    def draw(self):
        pass