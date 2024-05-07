import pygame

# import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Sterion', 20)
pygame.display.set_caption("Space Attack!")

# set up variables for the display
start_size = (700, 400)
start_screen = pygame.display.set_mode(start_size)

bg_start = pygame.image.load("starter-spacebackground.jpg")

bg_lvl1 = pygame.image.load("lvl1-background.jpg")

bg_start = pygame.transform.scale(bg_start, (700, 400))
bg_lvl1 = pygame.transform.scale(bg_lvl1, (700, 400))

background_sound = pygame.mixer.music.load('space_signal_sound.mp3')
pygame.mixer.music.play(-1)

welcome_message = "This is space mission over. "

# variables:
start = False

# render the text for later


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------


while run:
    # --- Main event loop

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start = True
            size = (700, 400)
            start_screen = pygame.display.set_mode(size)
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    if not start:
        start_screen.blit(bg_start, (0, 0))
    if start:
        start_screen.blit(bg_lvl1, (0, 0))
    pygame.display.update()