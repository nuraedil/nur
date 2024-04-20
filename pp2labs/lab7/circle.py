import pygame

pygame.init()

# Определяем размеры экрана и создаем его
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Устанавливаем заголовок окна
pygame.display.set_caption("Moving Circle")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные координаты и скорость перемещения круга
x, y = WIDTH // 2, HEIGHT // 2
speed = 20

# Основной цикл программы
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)  # Очищаем экран белым цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Проверяем нажатые клавиши
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y >= 41:
        y -= speed
    if keys[pygame.K_DOWN] and y <= HEIGHT - 41:
        y += speed
    if keys[pygame.K_LEFT] and x >= 41:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= WIDTH - 41:
        x += speed

    # Рисуем круг
    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.update()  # Обновляем экран
    clock.tick(60)  # Устанавливаем FPS

pygame.quit()
