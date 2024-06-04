import pygame
import random
import time
from playerspaceship import PlayerSpaceShip
#from playerbullets import PlayerBullets
from enemyspaceship1 import EnemySpaceShip1
from enemyspaceship2 import EnemySpaceShip2
from button import Button
from enemybullets import EnemyBullets
from enemyspaceship3 import EnemySpaceShip3
# from playerspaceshipnew import PlayerSpaceShipNew
# from playerbulletsnew import PlayerBulletsNew

# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Sterion', 60)
text_font = pygame.font.SysFont('Speedy', 30)
pygame.display.set_caption("Space Attack!")

# set up variables for the display
start_size = (1000, 500)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
start_screen = pygame.display.set_mode(start_size)

bg_start = pygame.image.load("starter-spacebackground.jpg")

bg_lvl1 = pygame.image.load("lvl1-background.jpg")

bg_start = pygame.transform.scale(bg_start, (1000, 500))
bg_lvl1 = pygame.transform.scale(bg_lvl1, (1000, 500))


# player
ps = PlayerSpaceShip(400, 400)
#pb = PlayerBullets(ps.x + 10, ps.y + 10)


# player bullets
player_bullet = pygame.image.load("player_bullet.png")
player_bullet = pygame.transform.scale(player_bullet, (30, 40))
player_bulletX = 0
player_bulletY = 480
player_bulletX_change = 0
player_bulletY_change = 8
player_bullet_state = "ready"

sb = Button(400, 400)

background_sound = pygame.mixer.music.load('space_signal_sound.mp3')
pygame.mixer.music.play(-1)

# sprite groups
player_spaceship_group = pygame.sprite.Group()
player_bullets_group = pygame.sprite.Group()

# text on screen
title = "SPACE ATTACK"
message1 = "THIS IS SPACE CONTROL OVER. THE UNIVERSE NEEDS YOUR HELP."
message2 = "ALIENS ARE ATTACKING THE MILKYWAY GALAXY."
instruction1 = "Use your space battleship bullets to counter their attacks."
instruction2 = "Keys: use spacebar to launch bullets and the arrow keys to move."

# variables:
start = False
enemy_hit = False

INITIAL_BG_LVL1_Y = random.randint(0,500)
bg_lvl1_y = INITIAL_BG_LVL1_Y


# player health stuff
player_health = 100
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)


# enemy spaceships
es1 = EnemySpaceShip1(400,  50)
es1_speed = 2
es1_flying = False

es2 = EnemySpaceShip2(700,  50)
es2_speed = 2
es2_flying = False

es3 = EnemySpaceShip3(200, 50)
es3_speed = 2
es3_flying = False



# render the text for later
display_title = title_font.render(title, True, (255, 255, 255))
display_message1 = text_font.render(message1, True, (255, 255, 255))
display_message2 = text_font.render(message2, True, (255, 255, 255))
display_instruction1 = text_font.render(instruction1, True, (255, 255, 255))
display_instruction2 = text_font.render(instruction2, True, (255, 255, 255))

# bullet function
def fire_bullet(x, y):
    global player_bullet_state
    player_bullet_state = "fire"
    start_screen.blit(player_bullet,(x + 16, y + 30))

# player_bullet-enemy spaceships collision function:
def collision_w_es1(es1.x, )

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
clock = pygame.time.Clock()
# -------- Main Program Loop -----------

while run:
    # --- Main event loop
    clock.tick(60)
    if start == True:
        bg_lvl1_y -= 100
        if bg_lvl1_y < -300:
            bg_lvl1_y = random.randint(500, 1000)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            if sb.rect.collidepoint(event.pos):
                start = True
                size = (1000, 500)
                start_screen = pygame.display.set_mode(size)
        # shooting player bullets
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            player_bulletX = ps.x
            fire_bullet(ps.x, player_bulletY)

        if event.type == pygame.MOUSEBUTTONDOWN:
            player_health -= 5
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    # movement for player spaceship
    keys_player = pygame.key.get_pressed()  # checking pressed keys
    if keys_player[pygame.K_RIGHT]:
        ps.move_player_ship("right")
    if keys_player[pygame.K_LEFT]:
        ps.move_player_ship("left")


    # enemy spaceships
    if start:
         es1_flying = True
         es2_flying = True
         es3_flying = True
         if es1_flying:
             es1.y += es1_speed
             es1.rect.y = es1.y
             if es1.rect.y > SCREEN_HEIGHT:
                es1.y = es1.rect.y
                es1.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
             elif es1.rect.y > SCREEN_HEIGHT:
                es1.y = es1.rect.y
                es1.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
         if es2_flying:
             es2.y += es2_speed
             es2.rect.y = es2.y
             if es2.rect.y > SCREEN_HEIGHT:
                 es2.y = es2.rect.y
                 es2.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
             elif es2.rect.y > SCREEN_HEIGHT:
                 es2.y = es2.rect.y
                 es2.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
         if es3_flying:
             es3.y += es3_speed
             es3.rect.y = es3.y
             if es3.rect.y > SCREEN_HEIGHT:
                 es3.y = es3.rect.y
                 es3.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
             elif es3.rect.y > SCREEN_HEIGHT:
                 es3.y = es3.rect.y
                 es3.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)

    if not start:
        start_screen.blit(bg_start, (0, 0))
        start_screen.blit(display_title, (250, 50))
        start_screen.blit(display_message1, (230, 120))
        start_screen.blit(display_message2, (230, 160))
        start_screen.blit(display_instruction1, (230, 220))
        start_screen.blit(display_instruction2, (230, 260))
        start_screen.blit(sb.image, sb.rect)
    if start:
        start_screen.blit(bg_lvl1, (0, 0))
        start_screen.blit(ps.image, ps.rect)
        # player_spaceship_group.draw(start_screen)
        # player_spaceship_group.update()
        start_screen.blit(es1.image, es1.rect)
        start_screen.blit(es2.image, es2.rect)
        start_screen.blit(es3.image, es3.rect)
        # pygame.draw.rect(start_screen, RED, (200, 400, 100, 5))
        # pygame.draw.rect(start_screen, GREEN, (200, 400, player_health, 5))
        # if keys_player[pygame.K_SPACE]:
        #     start_screen.blit(pb.image, pb.rect)
        if player_bulletY <= 0:
            player_bulletY = 480
            player_bullet_state = "ready"
        if player_bullet_state == "fire":
            fire_bullet(player_bulletX, player_bulletY)
            player_bulletY -= player_bulletY_change

    pygame.display.update()