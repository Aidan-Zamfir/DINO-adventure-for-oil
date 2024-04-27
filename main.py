import pygame
import os
import random

pygame.init()

# GLOBAL VARS:

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
DUCK = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
JUMP = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
SMALL_CAC = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
             pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CAC = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
            pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
PLANE = [pygame.image.load(os.path.join("Assets/Plane", "Freedom1.png")),
            pygame.image.load(os.path.join("Assets/Plane", "LiberationUnit.png"))]
ARMY = [pygame.image.load(os.path.join("Assets/Army", "Tank2.png")),
            pygame.image.load(os.path.join("Assets/Army", "Tent2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
OIL = pygame.image.load(os.path.join("Assets/Oil", "Oil.png"))
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.duck_img = DUCK
        self.run_img = RUN
        self.jump_img = JUMP

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        SCREEN.fill((255, 255, 255))


    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        self.jump_velocity = self.JUMP_VELOCITY

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_velocity * 4.2
            self.jump_velocity -= 0.6
        if self.jump_velocity < - self.JUMP_VELOCITY:
            self.dino_jump = False
            self.jump_velocity = self.JUMP_VELOCITY

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()


    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacles:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCac(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCac(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacles):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class Plane(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 100

class Oil:
    def __init__(self, image, p_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos_y = p_y


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.pos_y,230))


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = Cloud()
    game_speed = 13
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    pos_Y = 1090

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 0.5

        text = font.render("SCORE: " + str(points), True, (0, 0 ,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg

        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    #game running:
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)



        if points <= 250:
            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(SmallCac(SMALL_CAC))
                elif random.randint(0, 2) == 1:
                    obstacles.append(LargeCac(LARGE_CAC))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Bird(BIRD))
        elif points >= 251 and points <= 350:
            Oil(OIL, pos_Y).draw(SCREEN)
            pos_Y -= 9
        elif points >= 401:
            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    pass
                elif random.randint(0, 2) == 1:
                    obstacles.append(LargeCac(ARMY))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Plane(PLANE))


        for i in obstacles:
            i.draw(SCREEN)
            i.update()
            if player.dino_rect.colliderect(i.rect):
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)


        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True

    while True:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press Any Key", True, (0, 0 ,0))
        elif death_count > 0:
            text = font.render("Press Any Key", True, (0, 0 ,0))
            score = font.render("SCORE: " + str(points), True, (0, 0 ,0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                main()


menu(death_count=0)

#make small army (3) rpl small cac

#Planes replace bird class/function (2) (IN SKY, change y)

#add oil
#add sound/music
#add flag

#change fonts