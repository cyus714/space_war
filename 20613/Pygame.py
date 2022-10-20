#20613
from cmath import rect
from turtle import width
import pygame

fps=60
WIDTH = 500
HEIGHT = 600

WHITE = (255,255,255)
GREEN=(0,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('第一個遊戲')
clock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image .fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0 


all_sprite = pygame.sprite.Group()
player = Player()




running= True
