import pygame
import random
from playerspaceship import PlayerSpaceShip

# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Sterion', 60)
text_font = pygame.font.SysFont('Speedy', 30)
pygame.display.set_caption("Space Attack!")

# set up variables for the display
start_size = (1000, 500)
start_screen = pygame.display.set_mode(start_size)

bg_start = pygame.image.load("starter-spacebackground.jpg")

bg_lvl1 = pygame.image.load("lvl1-background.jpg")

bg_start = pygame.transform.scale(bg_start, (1000, 500))
bg_lvl1 = pygame.transform.scale(bg_lvl1, (1000, 500))

start_button = pygame.image.load("button.png")
start_button = pygame.transform.scale(start_button, (200, 100))

ps = PlayerSpaceShip(300, 150)

background_sound = pygame.mixer.music.load('space_signal_sound.mp3')
pygame.mixer.music.play(-1)

# text on screen
title = "SPACE ATTACK"
message1 = "THIS IS SPACE CONTROL OVER. THE UNIVERSE NEEDS YOUR HELP."
message2 = "ALIENS ARE ATTACKING THE MILKYWAY GALAXY."
instruction1 = "Use your space battleship bullets to counter their attacks."
instruction2 = "Keys: use spacebar to launch bullets and the arrow keys to move."

# variables:
start = False

INITIAL_BG_LVL1_Y = random.randint(0,500)
bg_lvl1_y = INITIAL_BG_LVL1_Y


# render the text for later
display_title = title_font.render(title, True, (255, 255, 255))
display_message1 = text_font.render(message1, True, (255, 255, 255))
display_message2 = text_font.render(message2, True, (255, 255, 255))
display_instruction1 = text_font.render(instruction1, True, (255, 255, 255))
display_instruction2 = text_font.render(instruction2, True, (255, 255, 255))

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
            start = True
            size = (1000, 500)
            start_screen = pygame.display.set_mode(size)
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    # movement for player spaceship
    keys_player = pygame.key.get_pressed()  # checking pressed keys
    if keys_player[pygame.K_UP]:
        ps.move_player_ship("up")
    if keys_player[pygame.K_DOWN]:
        ps.move_player_ship("down")
    if keys_player[pygame.K_RIGHT]:
        ps.move_player_ship("right")
    if keys_player[pygame.K_LEFT]:
        ps.move_player_ship("left")

    if not start:
        start_screen.blit(bg_start, (0, 0))
        start_screen.blit(display_title, (250, 50))
        start_screen.blit(display_message1, (230, 120))
        start_screen.blit(display_message2, (230, 160))
        start_screen.blit(display_instruction1, (230, 220))
        start_screen.blit(display_instruction2, (230, 260))
        start_screen.blit(start_button, (230, 400))
    if start:
        start_screen.blit(bg_lvl1, (0, 0))
        start_screen.blit(ps.image, ps.rect)
    pygame.display.update()