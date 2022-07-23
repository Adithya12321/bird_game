import pygame, sys
from animations import *

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 280, 500
screen = pygame.display.set_mode((screen_width, screen_height))
start_time = pygame.time.get_ticks()
i = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                box.direction.y = -13
    screen.fill("black")
    background_group.draw(screen)
    background_group.update()
    if (pygame.time.get_ticks()-start_time)//1000 > 1:
        start_time = pygame.time.get_ticks()
        pos = random.randint(-250, -150)
        pipe_group.add(Pipe(pos, 1))
        pipe_group.add(Pipe(pos, -1))
    pipe_group.draw(screen)
    pipe_group.update()
    base_group.draw(screen)
    base_group.update()
    test_group.draw(screen)
    test_group.update()
    pygame.display.update()
    clock.tick(60)
