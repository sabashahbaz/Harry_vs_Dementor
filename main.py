import pygame
import os
from game import Game
from player import Player
from enemy import Enemy
from bullet import Bullet 

def main():
    
    pygame.init()

    game = Game()
    player = Player()
    enemy = Enemy ()
    bullet = Bullet ()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
  

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
