import pygame

# initializing pygame
pygame.init()

# setting screen
screen = pygame.display.set_mode((1000, 600))
running = True

# display text & icons
pygame.display.set_caption("Magnatiz")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# player icon
playerImg = pygame.image.load("player.png")
playerX = 450
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# background icon
# background = pygame.image.load("background.png")

# game loop
while running:
    # rgb - theme of screen
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keystroke movevent for the player.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 870:
        playerX = 870
    player(playerX, playerY)
    pygame.display.update()
