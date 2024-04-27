import pygame
import time
import random
import os

pygame.init()

# Параметры отображения
WIDTH, HEIGHT = 1200, 900
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Параметры игры
FPS = 10 
RUN = True
SCORE = 0
LEVEL = 1
level_added = False
fruit_spawn = True
black = (0, 0, 0)
red = (255, 0, 0)

# Загрузка изображений фруктов с измененными размерами
arbuze_image = pygame.transform.scale(pygame.image.load(os.path.join('food1.png')), (20, 20))
apelsin_image = pygame.transform.scale(pygame.image.load(os.path.join('food2.png')), (20, 20))
banana_image = pygame.transform.scale(pygame.image.load(os.path.join('food3.png')), (20, 20))

# Начальное направление змеи - вправо
direction = 'RIGHT'
change_to = direction

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.snake_position = [210, 60]  
        self.snake_body = [[210, 60], [180, 60], [150, 60], [120, 60]]  
        self.snake_color = (108, 187, 60)
        self.size_x, self.size_y = 30, 30

    def move(self, direction):
        if direction == "UP":
            self.snake_position[1] -= self.size_y
        if direction == "DOWN":
            self.snake_position[1] += self.size_y
        if direction == "LEFT":
            self.snake_position[0] -= self.size_x
        if direction == "RIGHT":
            self.snake_position[0] += self.size_x

    def grow(self):
        self.snake_body.insert(0, list(self.snake_position))

    def shrink(self):
        self.snake_body.pop()

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fruit_position = [random.randrange(0, (WIDTH // 30)) * 30, random.randrange(0, (HEIGHT // 30)) * 30]
        self.type = random.choice(["food1", "food2", "food3"])

    def update(self):
        self.fruit_position = [random.randrange(0, (WIDTH // 30)) * 30, random.randrange(0, (HEIGHT // 30)) * 30]
        self.type = random.choice(["food1", "food2", "food3"])

    def draw(self, surface):
        if self.type == "food1":
            surface.blit(arbuze_image, self.fruit_position)
        elif self.type == "food2":
            surface.blit(apelsin_image, self.fruit_position)
        elif self.type == "food3":
            surface.blit(banana_image, self.fruit_position)

S = Snake()
F = Fruit()

def draw_grid():
    for x in range(0, WIDTH, 30):
        pygame.draw.line(surface, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 30):
        pygame.draw.line(surface, (200, 200, 200), (0, y), (WIDTH, y))

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    level_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(SCORE), True, color)
    level_surface = level_font.render("Level : " + str(LEVEL), True, color)
    score_rect = score_surface.get_rect()
    score_rect.x, score_rect.y = 0, 0
    level_rect = level_surface.get_rect()
    level_rect.x, level_rect.y = 0, 30
    surface.blit(score_surface, score_rect)
    surface.blit(level_surface, level_rect)

while RUN:
    tickrate = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"

    if direction != "UP" and change_to == "DOWN":
        direction = "DOWN"
    if direction != "DOWN" and change_to == "UP":
        direction = "UP"
    if direction != "LEFT" and change_to == "RIGHT":
        direction = "RIGHT"
    if direction != "RIGHT" and change_to == "LEFT":
        direction = "LEFT"

    S.move(direction)

    S.grow()  
    
    if S.snake_position[0] == F.fruit_position[0] and S.snake_position[1] == F.fruit_position[1]:
        if F.type == "food1":
            SCORE += 1
        elif F.type == "food2":
            SCORE += 3
        elif F.type == "food3":
            SCORE += 5
        fruit_spawn = False
    else:
        S.shrink()
    
    if not fruit_spawn:
        F.update()
        fruit_spawn = True
    
    x = F.fruit_position[0] + 15
    y = F.fruit_position[1] + 15

    surface.fill((255, 255, 255))
    draw_grid()  
    for pos in S.snake_body:
        pygame.draw.rect(surface, (S.snake_color), pygame.Rect(pos[0], pos[1], S.size_x, S.size_y))
    
    F.draw(surface)

    if S.snake_position[0] < 0 or S.snake_position[0] > WIDTH - S.size_x:
        RUN = False
    if S.snake_position[1] < 0 or S.snake_position[1] > HEIGHT - S.size_y:
        RUN = False
    for body in S.snake_body[1:]:
        if S.snake_position[0] == body[0] and S.snake_position[1] == body[1]:
            RUN = False

    show_score(black, 'times new roman', 30)
    pygame.display.update()
    tickrate.tick(FPS)

time.sleep(1)
pygame.quit()
