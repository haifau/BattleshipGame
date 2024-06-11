import pygame
import random
import math
from playerspaceship import PlayerSpaceShip
from enemyspaceship1 import EnemySpaceShip1
from enemyspaceship2 import EnemySpaceShip2
from button import Button
from enemyspaceship3 import EnemySpaceShip3


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

# explosion
explosion = pygame.image.load("explosion.png")
explosion = pygame.transform.scale(explosion,(100, 100))

# player
ps = PlayerSpaceShip(400, 400)

# enemy spaceships
es1 = EnemySpaceShip1(400,  50)
es1_speed = 1
es1_flying = False

es2 = EnemySpaceShip2(700,  50)
es2_speed = 1
es2_flying = False

es3 = EnemySpaceShip3(200, 50)
es3_speed = 1
es3_flying = False

# player bullets
pb = pygame.image.load("player_bullet.png")
pb = pygame.transform.scale(pb, (30, 40))
pb_x = 0
pb_y = 480
pb_x_change = 0
pb_y_change = 8
pb_state = "ready"

# enemy1 bullets
eb1 = pygame.image.load("enemy_1_bullet.png")
eb1 = pygame.transform.scale(eb1, (30, 50))
eb1_x = es1.x
eb1_y = es1.y
eb1_x_change = 0
eb1_y_change = 5
eb1_state = "ready"

sb = Button(400, 400)

background_sound = pygame.mixer.music.load('space_battle_sound.mp3')
pygame.mixer.music.play(-1)

# sprite groups
player_spaceship_group = pygame.sprite.Group()
player_bullets_group = pygame.sprite.Group()

# text on screen
title = "SPACE ATTACK"
message1 = "THIS IS SPACE CONTROL OVER. THE UNIVERSE NEEDS YOUR HELP."
message2 = "ALIENS ARE ATTACKING THE MILKYWAY GALAXY."
instruction1 = "Use your space battleship bullets to counter their attacks."
instruction2 = "Keys: use spacebar to launch bullets and the left/right keys to move."

# variables:
start = False
enemy_hit = False
launch_eb1 = False

INITIAL_BG_LVL1_Y = random.randint(0,500)
bg_lvl1_y = INITIAL_BG_LVL1_Y


# player health stuff
player_health = 100
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)




# render the text for later
display_title = title_font.render(title, True, (255, 255, 255))
display_message1 = text_font.render(message1, True, (255, 255, 255))
display_message2 = text_font.render(message2, True, (255, 255, 255))
display_instruction1 = text_font.render(instruction1, True, (255, 255, 255))
display_instruction2 = text_font.render(instruction2, True, (255, 255, 255))

# player_bullet function
def fire_bullet(x, y):
    global pb_state
    pb_state = "fire"
    start_screen.blit(pb,(x + 16, y + 30))

# enemy1_bullet function
def fire_enemy1_bullet(x, y):
    global eb1_state
    eb1_state = "fire"
    print('firing enemy bullet')
    start_screen.blit(eb1, (x + 20, y + 30))

# collision for player bullets and enemy spaceships function
def collide_w_es1(es1_x, es1_y, pb_x, pb_y):
    distance = math.sqrt((math.pow(es1_x - pb_x, 2)) + (math.pow(es1_y - pb_y, 2)))
    if distance < 60:
        return True
    else:
        return False

def collide_w_es2(es2_x, es2_y, pb_x, pb_y):
    distance = math.sqrt((math.pow(es2_x - pb_x, 2)) + (math.pow(es2_y - pb_y, 2)))
    if distance < 60:
        return True
    else:
        return False

def collide_w_es3(es3_x, es3_y, pb_x, pb_y):
    distance = math.sqrt((math.pow(es3_x - pb_x, 2)) + (math.pow(es3_y - pb_y, 2)))
    if distance < 60:
        return True
    else:
        return False

# collision for enemy bullets and player spaceship function
def eb1_collide_w_ps(ps_x, ps_y, eb1_x, eb1_y):
    distance = math.sqrt((math.pow(ps_x - eb1_x, 2)) + (math.pow(ps_y - eb1_y, 2)))
    if distance < 60:
        return True
    else:
        return False


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
            pb_x = ps.x
            fire_bullet(ps.x, pb_y)

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
             eb1_x = es1.x
             fire_enemy1_bullet(es1.x, eb1_y)
             if es1.rect.y > SCREEN_HEIGHT:
                es1.y = es1.rect.y
                es1.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
         es1_x = es1.x
         es1_y = es1.y
         if es2_flying:
             es2.y += es2_speed
             es2.rect.y = es2.y
             if es2.rect.y > SCREEN_HEIGHT:
                 es2.y = es2.rect.y
                 es2.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
             es2_x = es2.x
             es2_y = es2.y
         if es3_flying:
             es3.y += es3_speed
             es3.rect.y = es3.y
             if es3.rect.y > SCREEN_HEIGHT:
                 es3.y = es3.rect.y
                 es3.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
             es3_x = es3.x
             es3_y = es3.y


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
        launch_eb1 = True
        if launch_eb1:
            if eb1_y <= 0:
                eb1_y = 50
                eb1_state = "ready"
            if eb1_state == "fire":
                fire_enemy1_bullet(eb1_x, eb1_y)
                eb1_y += eb1_y_change
        start_screen.blit(ps.image, ps.rect)
        start_screen.blit(es1.image, es1.rect)
        start_screen.blit(es2.image, es2.rect)
        start_screen.blit(es3.image, es3.rect)
        pygame.draw.rect(start_screen, RED, (ps.x, ps.y, 100, 5))
        pygame.draw.rect(start_screen, GREEN, (ps.x, ps.y, player_health, 5))
        if pb_y <= 0:
            pb_y = 480
            pb_state = "ready"
        if pb_state == "fire":
            fire_bullet(pb_x, pb_y)
            pb_y -= pb_y_change

        collision_w_es1 = collide_w_es1(es1_x, es1_y, pb_x, pb_y)

        if collision_w_es1:
            pb_y = 480
            pb_state = "ready"
            es1.update()
            start_screen.blit(explosion, (es1_x, es1_y))

        collision_w_es2 = collide_w_es2(es2_x, es2_y, pb_x, pb_y)

        if collision_w_es2:
            pb_y = 480
            pb_state = "ready"
            start_screen.blit(explosion, (es2_x, es2_y))

        collision_w_es3 = collide_w_es3(es3_x, es3_y, pb_x, pb_y)

        if collision_w_es3:
            pb_y = 480
            pb_state = "ready"
            start_screen.blit(explosion, (es3_x, es3_y))

        ps_x = ps.x
        ps_y = ps.y

        eb1_collision_w_ps = eb1_collide_w_ps(ps_x, ps_y, eb1_x, eb1_y)

        if eb1_collision_w_ps:
            eb1_y = 50
            pb_state = "ready"
            player_health -= 5


    pygame.display.update()