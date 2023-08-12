import pygame
import os
from game import Game
pygame.font.init()

USER_IMAGE = pygame.image.load(os.path.join('../Assets', 'user.png'))


# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
user_bullets = []
RED = (255, 0, 0)
BLACK = (0,0,0)
# BORDER = pygame.Rect(900//2 -5, 0, 5, 500)

#initiating the player class with its width, height and position 
class Player(Game):
    def __init__(self):
        super().__init__()
        self.player_width = 100
        self.player_height = 150
        self.player_x = 320
        self.player_y = 590
        self.player_vel = 5
    
    #Setting the image of the sprite
    def draw_player(self):
        self.user_image = pygame.transform.rotate(pygame.transform.scale(USER_IMAGE, (self.player_width, self.player_height)), 0)
        self.window.blit(self.user_image, (self.player_x, self.player_y))
        # pygame.draw.rect(self.window, BLACK, BORDER)
        # for bullet in user_bullets:
        #     pygame.draw.rect(self.window,RED, bullet)

    #defining the keys that are pressed and moving the player
    #checking to see which keys are pressed 
    def player_movement(self):
        keys_pressed = pygame.key.get_pressed() #
        if keys_pressed[pygame.K_LEFT] and self.player_x >= 0: #left (if player x position minus vel <0 )
            self.player_x -= self.player_vel
        if keys_pressed[pygame.K_RIGHT] and self.player_x + self.player_width < self.win_width: #right
            self.player_x += self.player_vel
        if keys_pressed[pygame.K_UP] and self.player_y >= 0: #up
            self.player_y -= self.player_vel
        if keys_pressed[pygame.K_DOWN] and self.player_y + self.player_height < self.win_height: #down
            self.player_y += self.player_vel

    #displaying the points of the player 
    def player_display_points(self):
        points = 0 
        dementor_lives =10
        self.font = pygame.font.SysFont("Verdana", 30)
        points_label = self.font.render(f"points: {points}", 1, (255, 255, 255))
        lives_label = self.font.render(f"dementor lives: {dementor_lives}", 1, (255, 255, 255))
        self.window.blit(points_label, (10,10))
        self.window.blit(lives_label, (self.win_width - lives_label.get_width() -10, 10))


#pressing the space bar and having a bullet fired





