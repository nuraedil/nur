import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Moving Circle")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
speed = 20


running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y >= 41:
        y -= speed
    if keys[pygame.K_DOWN] and y <= HEIGHT - 41:
        y += speed
    if keys[pygame.K_LEFT] and x >= 41:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= WIDTH - 41:
        x += speed

    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.update()  
    clock.tick(60) 

pygame.quit()
