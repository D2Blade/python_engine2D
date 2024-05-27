import pygame
from pygame.locals import *
from settings import *

janela_config = windowConf(600,600)
janela = janela_config.create_window()

player_config = playerConf(GREEN, janela_config.largura / 2, janela_config.altura / 2, 30, 30)

frames = pygame.time.Clock()
run = True
while run:
    frames.tick(40)
    janela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if event.type == KEYDOWN:
            if event.key == K_q:
                run = False
    player_config.top_down_move()
    player_config.create_player(janela)
    print(frames)
    pygame.display.update()
pygame.quit()