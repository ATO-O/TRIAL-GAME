import pygame

# initializing pygame
pygame.init()

# setting screen
screen = pygame.display.set_mode((800, 600))
running = True

#display text & icons
pygame.display.set_caption("Magnatiz")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #rgb - theme of screen
    screen.fill((0, 0, 255))
    pygame.display.update()


