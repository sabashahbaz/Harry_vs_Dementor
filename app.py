import pygame
import os 
# from player_class import Player

#initiating pygame library
pygame.init()

#setting the size of the window 
WIN = pygame.display.set_mode((700,700))
BLUE = (0,255,255)
#caption of the game 
pygame.display.set_caption("Harry Potter vs Dementors") 

#setting the images of the background and sprites 
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Room_of_Requirement.png')),(700, 700))
USER_IMAGE = pygame.image.load(os.path.join('Assets', 'user.png'))
ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'death_eater.png'))


#render images on the game window by calling the specific methods 
def drawGameWindow():
    WIN.blit(BACKGROUND_IMAGE, (0,0))
    player.draw_player()
    enemy.draw_enemy()
    for bullet in player_bullets:
        bullet.draw_bullet()
    player.player_display_points()

    pygame.display.update()

class Player(object):
    #initiating the player sprite
    def __init__(self,x,y,width,height):
        #player's position is on the window 
        self.player_x = x
        self.player_y = y
        #player's height and width
        self.player_width = width
        self.player_height = height
        self.player_vel = 5 #velocity when it moves 

    #method to display the player
    def draw_player(self):
        self.player_hit_box = (self.player_x + 15, self.player_y + 30 - 10, 60, 100)
        #pygame.draw.rect(WIN, (255,0,0), self.player_hit_box,2)
        self.user_image = pygame.transform.rotate(pygame.transform.scale(USER_IMAGE, (self.player_width, self.player_height)), 0)
        WIN.blit(self.user_image, (self.player_x, self.player_y))

    #method to move the player by pressing the specifc keys
    def player_movement(self):
        keys_pressed = pygame.key.get_pressed() #
        if keys_pressed[pygame.K_LEFT] and self.player_x >= 0: #left 
            self.player_x -= self.player_vel
        if keys_pressed[pygame.K_RIGHT] and self.player_x + self.player_width < 700: #right
            self.player_x += self.player_vel
        if keys_pressed[pygame.K_UP] and self.player_y >= 0: #up
            self.player_y -= self.player_vel
        if keys_pressed[pygame.K_DOWN] and self.player_y + self.player_height < 700: #down
            self.player_y += self.player_vel

    #display the points earned when hitting the dementor 
    def player_display_points(self):
        self.font = pygame.font.SysFont("Verdana", 30)
        points_label = self.font.render(f"points: {player_points}", 1, (255, 255, 255))
        WIN.blit(points_label, (10,10))

class Enemy(object):
    #initiating the player sprite
    def __init__(self,x,y,width,height):
        #enemy's position on the window 
        self.enemy_x = x
        self.enemy_y = y
        #enemy's height and width
        self.enemy_width = width
        self.enemy_height = height
        self.enemy_vel = 6
        self.left = True
        self.enemy_hit_box = (self.enemy_x, self.enemy_y, 60, 100) #defining where the bullet hits the enemy 

    #method to display the enemy
    def draw_enemy(self):
        self.enemy_hit_box = (self.enemy_x + 15, self.enemy_y + 10 , 60, 100) #hitbox around the enemy sprite, so when the bulllet hits the enemy it will trigger collision reaction (60 = width of hit box 100 = height)
        self.user_image = pygame.transform.rotate(pygame.transform.scale(ENEMY_IMAGE, (self.enemy_width, self.enemy_height)), 0)
        WIN.blit(self.user_image, (self.enemy_x, self.enemy_y))
    
    #enemy moving across the screen 
    def move_enemy(self):
        if self.left: #this is set to true
            self.enemy_x -= self.enemy_vel #move the enemy to the left, by negating the direction of the enemy velcoty to decrease the x-coordinate  
        else:
            self.enemy_x += self.enemy_vel #move the enemy to the right, increasing the x-coordinate 

        # Check if the dementor has reached to the edge of the screen 
        if self.enemy_x < 0: #enemy has reached the left edge on the window 
            self.left = False #change the value of self.left -> this triggers a change in move_enemy()
        elif self.enemy_x + self.enemy_width >= 700: #enemy reached the right edge on the window 
            self.left = True 
    
        assert self.enemy_x + self.enemy_width

    # def hit_enemy(self):
    #     print("hit")

class Bullet(Player):
    #initiating the bullet
    def __init__(self,x,y,radius, color):
        self.bullet_x = x
        self.bullet_y = y
        self.radius = radius
        self.color = color
        self.bullet_vel = 7
    
    #method to display the bullet
    def draw_bullet(self):
        pygame.draw.circle(WIN, self.color,(self.bullet_x, self.bullet_y), self.radius)

#MAIN LOOP
player = Player(350, 590, 100, 150) #specifing the player's attributes 
enemy = Enemy (700, 100, 100, 150)  #specifing the enemy's attributes 
bullet_cooldown = 0
player_points = 0
player_bullets = [] #the initial empty list of the player's bullets 
run = True
enemybullets = True

#Defining hit_box dimensions 
bottom_of_enemy_hit_box = (enemy.enemy_y + 10) + 60 
width_of_enemy_hit_box = 60 
left_of_enemy_hit_box = enemy.enemy_hit_box[0]




#the main game loop 
while run:
    #contorl the frame rate of game loop to be 60 frames per second
    clock = pygame.time.Clock()
    clock.tick(60)

    #cooldown period between bullet shots, to avoid mutiple bullets being fired at the same time 
    if bullet_cooldown > 0: #initially set to 0, but when user fires a bullet, bullet_cooldown increases by 1
        bullet_cooldown += 1
    if bullet_cooldown > 10: #when 10 frames per loop pass 
        bullet_cooldown = 0 #now the user can shoot the bullet again 

    #going through each event in the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when the user clicks the x on the window, the game will quit 
            run = False #stop the game loop 

    #when the bullet hits the enemy 
    for bullet in player_bullets:
        if bullet.bullet_y - bullet.radius < enemy.enemy_hit_box[1] + enemy.enemy_hit_box[3] and bullet.bullet_y - bullet.radius > enemy.enemy_hit_box[1]:
            if bullet.bullet_x - bullet.radius > enemy.enemy_hit_box[0] and bullet.bullet_x - bullet.radius < enemy.enemy_hit_box[0] + enemy.enemy_hit_box[2]:
                # enemy.hit_enemy()
                player_points += 1
                player_bullets.pop(player_bullets.index(bullet)) 
        if bullet.bullet_y < 700 and bullet.bullet_y > 0:
            bullet.bullet_y -= bullet.bullet_vel
        else: 
            player_bullets.pop(player_bullets.index(bullet)) 
    
    #key funtion to shoot the bullet 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and bullet_cooldown == 0: 
        if len(player_bullets) < 10:
            player_bullets.append(Bullet(round(player.player_x + player.player_width //2), round(player.player_y + player.player_height//2), 6, (BLUE)))
        bullet_cooldown = 1 

    #calling the methods
    drawGameWindow()
    player.player_movement()
    enemy.move_enemy()
    

pygame.quit()

#self.enemy_hit_box = (self.enemy_x, self.enemy_y, 60, 100)
    #enemy.enemy_hit_box[0] = x-coordinate 
    #enemy.enemy_hit_box[1] = y-coordinate
    #enemy.enemy_hit_box[2] = width 
    #enemy.enemy_hit_box[3] = height 