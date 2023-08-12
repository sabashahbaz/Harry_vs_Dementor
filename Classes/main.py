import pygame
import os
from game import Game
from player import Player
from enemy import Enemy
from bullet import Bullet 

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
    while run: #while the game is running (defined above)
        clock.tick(60) #speed of the game loop -> 60 frames per second
        for event in pygame.event.get(): #iterates over all the events in pygame 
            if event.type == pygame.QUIT: #when user clicks the x on the window, quits game 
                run = False #if game is quit, ends the while loop of the game running. 

        #calling the methods from the respective classes
        game.draw_window() #display background 

        player.draw_player() #display player on screen 
        player.player_movement() #function for pressing key and moving player
        player.player_display_points() #display the points 
         
        enemy.draw_enemy()
        enemy.update()
        enemy.enemy_display_points()
        
        bullet.bullet_movement()
  
    pygame.quit()

if __name__ == "__main__":
    main()
