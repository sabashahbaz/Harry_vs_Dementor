import pygame
import os
from player import Player
from game import Game
from enemy import Enemy
pygame.mixer.init()

BLUE = (209,238,238)
BULLET_VEL = 7
# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# class Bullet(Player, Game, pygame.sprite.Sprite):
#     def __init__ (self):
#         self.player_bullets = []
#         self.bullet_vel = 7
#         self.max_bullets= 100
#         # self.dementor_hit = pygame.USEREVENT + 2

#     def player_bullet(self):
#         for bullet in self.player_bullets:
#             pygame.draw.rect(self.window, BLUE, bullet)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite(self)
        self.image = pygame.image.load("Assets/laser.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y -= 5 
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            bullet = Bullets(self.rect.centerx, self.rect.top)

    