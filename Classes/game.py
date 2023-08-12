import pygame
import os

pygame.display.set_caption("Harry vs Dementor")

#setting the window of the game 
class Game: 
    def __init__(self):
        self.win_width = 700
        self.win_height = 750
        self.window = pygame.display.set_mode((self.win_width, self.win_height))
        self.background = pygame.transform.scale(pygame.image.load(
            os.path.join('../Assets', 'Room_of_Requirement.png')), (self.win_width, self.win_height))
        
    
    def draw_window(self):
        # self.background = self.window.blit(self.background, (0,0))
        self.window.blit(self.background, (0, 0))

        

    