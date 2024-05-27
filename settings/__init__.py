import pygame
from pygame.locals import *
from settings import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class windowConf:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.window = None

    def create_window(self):
        self.window = pygame.display.set_mode((self.largura,self.altura))
        return self.window

class playerConf:
    def __init__(self, cor, x, y, player_largura, player_altura):
        self.cor = cor
        self.x = x
        self.y = y
        self.player_largura = player_largura
        self.player_altura = player_altura

    def create_player(self, window):
        self.player_spawn = pygame.draw.rect(window ,self.cor ,(self.x, self.y, self.player_largura, self.player_altura))
        return self.player_spawn
    def top_down_move(self):
        if pygame.key.get_pressed()[K_a]:
            self.x = self.x - 10
        if pygame.key.get_pressed()[K_d]:
            self.x = self.x + 10
        if pygame.key.get_pressed()[K_w]:
            self.y = self.y - 10
        if pygame.key.get_pressed()[K_s]:
            self.y = self.y + 10
