import pygame
#import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Space Attack!")


# set up variables for the display
start_size = (618, 360)
start_screen = pygame.display.set_mode(start_size)

bg_start = pygame.image.load("starter-spacebackground.jpg")


bg_lvl1 = pygame.image.load("lvl1-background.jpg")


#title = ["ARRR! Ahoy matey! Captain Hook told me you'll come.", "Welcome to the Blue Lagoon Island!", "You have to find as many golden treasure", "as you can before the other pirates!", "It won't be easy. You will also have to deal", "with other enemies of the sea.", "Let's see if you make it out alive."]

# variables:
start = False

# render the text for later


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------

while run:
    # --- Main event loop

    while start == False:
        y_offset = 5
        #for line in title:
            #title_text = my_font.render(line, True, (255, 255, 255))
            #screen.blit(title_text, (620/2, y_offset))
            #y_offset += 5


    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start = True
            size = (612, 362)
            screen = pygame.display.set_mode(size)
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    if not start:
        screen.blit(bg_start, (0, 0))
    if start:
        screen.blit(bg_lvl1, (0, 0))
    pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

