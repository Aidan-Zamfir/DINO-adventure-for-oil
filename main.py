import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

RUN = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

JUMP = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]

DUCK = [pygame.image.load(os.path.join("Assets/Dino", "DinDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CAC = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CAC = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
            pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]

#add USA later