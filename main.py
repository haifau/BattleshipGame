import pygame
import random
import math
from playerspaceship import PlayerSpaceShip
from button import Button
from enemyspaceship1 import EnemySpaceShip1
from enemyspaceship2 import EnemySpaceShip2
from enemyspaceship3 import EnemySpaceShip3
from spacerock import SpaceRock


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

# space rock
sr = SpaceRock(900, 50)
sr_speed = 2
sr_flying = False
sr_collide_ps = True

# enemy spaceships
es1 = EnemySpaceShip1(400,  50)

es2 = EnemySpaceShip2(700,  50)

es3 = EnemySpaceShip3(200, 50)


# player bullets
pb = pygame.image.load("player_bullet.png")
pb = pygame.transform.scale(pb, (30, 40))
pb_x = ps.x
pb_y = ps.y
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

# enemy2 bullets
eb2 = pygame.image.load("enemy_2_bullet.png")
eb2 = pygame.transform.scale(eb2, (30, 50))
eb2_x = es2.x
eb2_y = es2.y
eb2_x_change = 0
eb2_y_change = 5
eb2_state = "ready"

# enemy3 bullets
eb3 = pygame.image.load("enemy_3_bullet.png")
eb3 = pygame.transform.scale(eb3, (30, 50))
eb3_x = es3.x
eb3_y = es3.y
eb3_x_change = 0
eb3_y_change = 5
eb3_state = "ready"

sb = Button(400, 430)

background_sound = pygame.mixer.music.load('space_battle_sound.mp3')
pygame.mixer.music.play(-1)

# text on screen
title = "SPACE ATTACK"
message1 = "THIS IS SPACE CONTROL OVER. THE UNIVERSE NEEDS YOUR HELP."
message2 = "ALIENS ARE ATTACKING THE MILKYWAY GALAXY."
instruction1 = "Use your space battleship bullets to counter their attacks."
instruction2 = "Player keys: spacebar = bullets & arrow keys for movement."
instruction3 = "Enemy 1 (blue) keys: 7 = bullets & 8624 keys for movement."
instruction4 = "Enemy 2 (white) keys: O = bullets & ILKJ keys for movement."
instruction5 = "Enemy 3 (brown) keys: Q = bullets & WDSA keys for movement."

# variables:
start = False

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
display_instruction3 = text_font.render(instruction3, True, (255, 255, 255))
display_instruction4 = text_font.render(instruction4, True, (255, 255, 255))
display_instruction5 = text_font.render(instruction5, True, (255, 255, 255))

# player_bullet function
def fire_bullet(x, y):
    global pb_state
    pb_state = "fire"
    start_screen.blit(pb,(x + 16, y + 30))

# enemy1_bullet function
def fire_enemy1_bullet(x, y):
    global eb1_state
    eb1_state = "fire"
    start_screen.blit(eb1, (x + 16, y + 30))

# enemy2_bullet function
def fire_enemy2_bullet(x, y):
    global eb2_state
    eb2_state = "fire"
    start_screen.blit(eb2, (x + 16, y + 30))

# enemy3_bullet function
def fire_enemy3_bullet(x, y):
    global eb3_state
    eb3_state = "fire"
    start_screen.blit(eb3, (x + 16, y + 30))

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

def eb2_collide_w_ps(ps_x, ps_y, eb2_x, eb2_y):
    distance = math.sqrt((math.pow(ps_x - eb2_x, 2)) + (math.pow(ps_y - eb2_y, 2)))
    if distance < 60:
        return True
    else:
        return False

def eb3_collide_w_ps(ps_x, ps_y, eb3_x, eb3_y):
    distance = math.sqrt((math.pow(ps_x - eb3_x, 2)) + (math.pow(ps_y - eb3_y, 2)))
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
            pb_y = ps.y
            fire_bullet(ps.x, ps.y)

        # shooting enemy bullets
        key_eb1 = pygame.key.get_pressed()
        if key_eb1[pygame.K_7]:
            eb1_x = es1.x
            eb1_y = es1.y
            fire_enemy1_bullet(es1.x, es1.y)
        key_eb2 = pygame.key.get_pressed()
        if key_eb2[pygame.K_q]:
            eb2_x = es2.x
            eb2_y = es2.y
            fire_enemy2_bullet(es2.x, es2.y)
        key_eb3 = pygame.key.get_pressed()
        if key_eb3[pygame.K_o]:
            eb3_x = es3.x
            eb3_y = es3.y
            fire_enemy3_bullet(es3.x, es3.y)

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    # movement for player spaceship
    keys_player = pygame.key.get_pressed()  # checking pressed keys
    if keys_player[pygame.K_RIGHT]:
        ps.move_player_ship("right")
    if keys_player[pygame.K_LEFT]:
        ps.move_player_ship("left")
    if ps.x <= 10:
        ps.x = 10
    elif ps.x >= 880:
        ps.x = 880
    if keys_player[pygame.K_UP]:
        ps.move_player_ship("up")
    if keys_player[pygame.K_DOWN]:
        ps.move_player_ship("down")
    if ps.y <= 10:
        ps.y = 10
    elif ps.y >= 380:
        ps.y = 380


    # movement for enemy spaceships

    # enemy 1
    keys_enemy1 = pygame.key.get_pressed()  # checking pressed keys
    if keys_enemy1[pygame.K_8]:
        es1.move_enemy1_ship("up")
    if keys_enemy1[pygame.K_6]:
        es1.move_enemy1_ship("right")
    if keys_enemy1[pygame.K_2]:
        es1.move_enemy1_ship("down")
    if keys_enemy1[pygame.K_4]:
        es1.move_enemy1_ship("left")
    if es1.x <= 10:
        es1.x = 10
    elif es1.x >= 880:
        es1.x = 880
    if es1.y <= 10:
        es1.y = 10
    elif es1.y >= 380:
        es1.y = 380
    es1_x = es1.x
    es1_y = es1.y

    # enemy 2
    keys_enemy2 = pygame.key.get_pressed()  # checking pressed keys
    if keys_enemy2[pygame.K_w]:
        es2.move_enemy2_ship("up")
    if keys_enemy2[pygame.K_d]:
        es2.move_enemy2_ship("right")
    if keys_enemy2[pygame.K_s]:
        es2.move_enemy2_ship("down")
    if keys_enemy2[pygame.K_a]:
        es2.move_enemy2_ship("left")
    if es2.x <= 10:
        es2.x = 10
    elif es2.x >= 880:
        es2.x = 880
    if es2.y <= 10:
        es2.y = 10
    elif es2.y >= 380:
        es2.y = 380
    es2_x = es2.x
    es2_y = es2.y

    # enemy 3
    keys_enemy3 = pygame.key.get_pressed()  # checking pressed keys
    if keys_enemy3[pygame.K_i]:
        es3.move_enemy3_ship("up")
    if keys_enemy3[pygame.K_l]:
        es3.move_enemy3_ship("right")
    if keys_enemy3[pygame.K_k]:
        es3.move_enemy3_ship("down")
    if keys_enemy3[pygame.K_j]:
        es3.move_enemy3_ship("left")
    if es3.x <= 10:
        es3.x = 10
    elif es3.x >= 880:
        es3.x = 880
    if es3.y <= 10:
        es3.y = 10
    elif es3.y >= 380:
        es3.y = 380
    es3_x = es3.x
    es3_y = es3.y

    if start:
        sr_flying = True
        if sr_flying:
            sr.y += sr_speed
            sr.rect.y = sr.y
            if sr.rect.y > SCREEN_HEIGHT:
                sr.y = sr.rect.y
                sr.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)

    if ps.rect.colliderect(sr.rect):
        sr_collide_ps = True
        if sr_collide_ps:
            player_health -= 7
            sr.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)


    if not start:
        start_screen.blit(bg_start, (0, 0))
        start_screen.blit(display_title, (250, 50))
        start_screen.blit(display_message1, (200, 120))
        start_screen.blit(display_message2, (200, 160))
        start_screen.blit(display_instruction1, (200, 220))
        start_screen.blit(display_instruction2, (200, 260))
        start_screen.blit(display_instruction3, (200, 300))
        start_screen.blit(display_instruction4, (200, 340))
        start_screen.blit(display_instruction5, (200, 380))
        start_screen.blit(sb.image, sb.rect)
    if start:
        start_screen.blit(bg_lvl1, (0, 0))
        start_screen.blit(ps.image, ps.rect)
        start_screen.blit(es1.image, es1.rect)
        start_screen.blit(es2.image, es2.rect)
        start_screen.blit(es3.image, es3.rect)
        start_screen.blit(sr.image, sr.rect)
        if sr_flying:
            sr.y += sr_speed
            sr.rect.y = sr.y
            if sr.rect.y > SCREEN_HEIGHT:
                sr.y = sr.rect.y
                sr.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.draw.rect(start_screen, RED, (ps.x, ps.y, 100, 5))
        pygame.draw.rect(start_screen, GREEN, (ps.x, ps.y, player_health, 5))
        if pb_y <= 0:
            pb_y = ps.y
            pb_state = "ready"
        if pb_state == "fire":
            fire_bullet(pb_x, pb_y)
            pb_y -= pb_y_change

        #collision for player bullets and enemy spaceships

        collision_w_es1 = collide_w_es1(es1_x, es1_y, pb_x, pb_y)

        if collision_w_es1:
            pb_y = 480
            pb_state = "ready"
            start_screen.blit(explosion, (es1.x, es1.y))

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

        # multiple enemy bullets
        # eb1
        if eb1_y <= 0:
            eb1_y = es1.y
            eb1_state = "ready"
        if eb1_state == "fire":
            fire_enemy1_bullet(eb1_x, eb1_y)
            eb1_y += eb1_y_change

        # eb2
        if eb2_y <= 0:
            eb2_y = es2.y
            eb2_state = "ready"
        if eb2_state == "fire":
            fire_enemy2_bullet(eb2_x, eb2_y)
            eb2_y += eb2_y_change

        # eb3
        if eb3_y <= 0:
            eb3_y = es3.y
            eb3_state = "ready"
        if eb3_state == "fire":
            fire_enemy3_bullet(eb3_x, eb3_y)
            eb3_y += eb3_y_change

        # collision for enemy bullets and player spaceship
        ps_x = ps.x
        ps_y = ps.y

        eb1_collision_w_ps = eb1_collide_w_ps(ps_x, ps_y, eb1_x, eb1_y)

        if eb1_collision_w_ps:
            player_health -= 3
            eb1_y = es1.y
            pb_state = "ready"

        eb2_collision_w_ps = eb1_collide_w_ps(ps_x, ps_y, eb2_x, eb2_y)

        if eb2_collision_w_ps:
            player_health -= 3
            eb2_y = es2.y
            pb_state = "ready"

        eb3_collision_w_ps = eb3_collide_w_ps(ps_x, ps_y, eb3_x, eb3_y)

        if eb3_collision_w_ps:
            player_health -= 3
            eb3_y = es3.y
            pb_state = "ready"


    pygame.display.update()