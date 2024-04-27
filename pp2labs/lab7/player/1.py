import pygame

pygame.init()

width, height = 3140, 2560

surface = pygame.display.set_mode((width, height))
name_pro = pygame.display.set_caption("Music player")

# Загрузка изображений 512 x 512
background = pygame.image.load('image/background.png')
stop_icon = pygame.image.load('image/stop_icon.png')
next_icon = pygame.image.load('image/next_icon.png')
previous_icon = pygame.image.load('image/previous_icon.png')
play_icon = pygame.image.load('image/play_icon.png')

# Загрузка музыки
pygame.mixer.music.load('music/1548068270_muzykalnyj-fajl.mp3')
pygame.mixer.music.load('music/dosekesh-taspa_(muzzonas.ru).mp3')
pygame.mixer.music.load('music/kairat-nurtas-irina-kairatovna-tun.mp3')

playlist = {
    1: 'music/1548068270_muzykalnyj-fajl.mp3',
    2: 'music/dosekesh-taspa_(muzzonas.ru).mp3',
    3: 'music/kairat-nurtas-irina-kairatovna-tun.mp3'
}

count_track = 1
run = True
FPS = 60
is_playing = False
tickrate = pygame.time.Clock()
paused_time = 0

while run:

    surface.blit(background, (0, 0))
    surface.blit(previous_icon, (100, 155))

    if is_playing == False:
        surface.blit(play_icon, (262, 155))
    else:
        surface.blit(stop_icon, (262, 155))

    surface.blit(next_icon, (424, 155))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_F7:
                if is_playing == False:
                    if paused_time != 0:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.load(playlist[count_track])
                        pygame.mixer.music.play()
                    is_playing = True
                else:
                    pygame.mixer.music.pause()
                    is_playing = False
                    paused_time = pygame.mixer.music.get_pos()
            elif event.key == pygame.K_F5 or event.key == pygame.K_LEFT:
                if count_track == 1:
                    count_track = 3
                else:
                    count_track -= 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif event.key == pygame.K_F6 or event.key == pygame.K_RIGHT:
                if count_track == 3:
                    count_track = 1
                else:
                    count_track += 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 100 <= mouse_x <= 156 and 155 <= mouse_y <= 211:  # Предыдущая кнопка
                if count_track == 1:
                    count_track = 3
                else:
                    count_track -= 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0
            elif 262 <= mouse_x <= 318 and 155 <= mouse_y <= 211:  # Кнопка Воспроизведение/Стоп
                if is_playing == False:
                    if paused_time != 0:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.load(playlist[count_track])
                        pygame.mixer.music.play()
                    is_playing = True
                else:
                    pygame.mixer.music.pause()
                    is_playing = False
                    paused_time = pygame.mixer.music.get_pos()
            elif 424 <= mouse_x <= 480 and 155 <= mouse_y <= 211:  # Следующая кнопка
                if count_track == 3:
                    count_track = 1
                else:
                    count_track += 1
                pygame.mixer.music.load(playlist[count_track])
                pygame.mixer.music.play()
                paused_time = 0

    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()
