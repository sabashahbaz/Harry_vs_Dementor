import pygame
import os
from game import Game
pygame.font.init()

USER_IMAGE = pygame.image.load(os.path.join('Assets', 'user.png'))
VEL = 5

# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
user_bullets = []
RED = (255, 0, 0)
BLACK = (0,0,0)
# BORDER = pygame.Rect(900//2 -5, 0, 5, 500)

class Player(Game):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 150
        self.x = 320
        self.y = 590
        self.vel = 5
    
    def draw_player(self):
        self.user_image = pygame.transform.rotate(pygame.transform.scale(USER_IMAGE, (self.width, self.height)), 0)
        self.window.blit(self.user_image, (self.x, self.y))
        # pygame.draw.rect(self.window, BLACK, BORDER)
        for bullet in user_bullets:
            pygame.draw.rect(self.window,RED, bullet)

    def player_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.x - VEL > 0: #left
            self.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and self.x + VEL + self.width < 720: #right
            self.x += VEL
        if keys_pressed[pygame.K_UP] and self.y - VEL > 0: #up
            self.y -= VEL
        if keys_pressed[pygame.K_DOWN] and self.y + VEL + self.height < 750 > 0: #down
            self.y += VEL

    def player_display_points(self):
        points = 0 
        dementor_lives =10
        self.font = pygame.font.SysFont("Verdana", 30)
        points_label = self.font.render(f"points: {points}", 1, (255, 255, 255))
        lives_label = self.font.render(f"dementor lives: {dementor_lives}", 1, (255, 255, 255))
        self.window.blit(points_label, (10,10))
        self.window.blit(lives_label, (700 - lives_label.get_width() -10, 10))


#pressing the space bar and having a bullet fired





