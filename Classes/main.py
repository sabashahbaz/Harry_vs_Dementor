import pygame
import os
from Classes.game import Game
from Classes.player import Player
from Classes.enemy import Enemy
from Classes.bullet import Bullet 

#call the methods from other classes
def main():
    
    pygame.init()

    #creating objects 
    game = Game()
    player = Player()
    enemy = Enemy ()
    bullet = Bullet ()

    #Ensuring the game runs at a constistent speed of 60 frames per second
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
  
        #calling the methods from the respective classes
        game.draw_window()

        player.draw_player()
        player.player_movement()
        player.player_display_points()
        
        enemy.draw_enemy()
        enemy.update()
        
        bullet.update()

    
    pygame.quit()

if __name__ == "__main__":
    main()
