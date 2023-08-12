import pygame
from game import Game
import os
import random
# from player import Player
# from game import Game
# from enemy import Enemy
pygame.mixer.init()



# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

BLUE = (209,238,238)

bullet_state = "ready" #can't see the bullet on screen  
#fire - bullet is currently moving 

class Bullet(Game):
    def __init__ (self):
        #establishing the bullet 
        self.bullet = pygame.image.load("../Assets/laser.png")
        self.bullet_vel = 7
        self.bulletY = 590
        self.bulletX = 0
        self.shoot = False

    def move_bullet (self):
        if self.shoot:
            self.y -= self.bullet_vel
        elif self.bullet.y < 0:
            self.shoot = False
      
    def draw_bullet(self):
        self.window.blit(self.bullet)
        pygame.display.update()

    def bullet_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            if self.shoot:
                self.y -= self.bullet_vel
            elif self.bullet.y < 700:
                self.bullet.remove(self.bullet)

    # def bullet_movement(self):
    #     # if self.bullet_state is "fire": 
    #     #     self.fire_bullet(320, self.bulletY)

    #     global bullet_state, bulletY
    #     if bullet_state == "fire":
    #         self.fire_bullet()
    #         bulletY -= self.bulletY

    #     if bulletY <= 0:
    #         bullet_state = "ready"
    #         bulletY = 590


# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))



    