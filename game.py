import pygame
import random

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

# coin icon
coinImg = pygame.image.load("silver-badge.png")
coinX = random.randint(0,1000)
coinY = 50
coinX_change = 0
coinY_change = 2

# paperclip icons
paperclipImg = pygame.image.load("paperclip.png")
paperclipX = random.randint(0,1000)
paperclipY = 50
paperclipX_change = 0
paperclipY_change = 2

# nut-bolt icons
nutImg = pygame.image.load("nut.png")
nutX = random.randint(0,1000)
nutY = 50
nutX_change = 0
nutY_change = 2

# bomb icons
bombImg = pygame.image.load("bomb.png")
bombX = random.randint(0,1000)
bombY = 50
bombX_change = 0
bombY_change = 2


def player(x, y):
    screen.blit(playerImg, (x, y))

#obstacles and collectible functions

def coin(x, y):
    screen.blit(coinImg, (x, y))


def paperclip(x, y):
    screen.blit(paperclipImg, (x, y))


def nut(x, y):
    screen.blit(nutImg, (x, y))


def bomb(x, y):
    screen.blit(bombImg, (x, y))


# background icon
background = pygame.image.load("background.png")

# game loop
while running:
    # rgb - theme of screen
    screen.fill((0, 0, 255))
    #background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke movevent for the player.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
#player movement boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 870:
        playerX = 870

    coinY += coinY_change
#coin movement boundries
    if coinY <= 0:
        coinY = 0
    elif coinY >= 450:
        coinY = 450

    nutY += nutY_change
# nut movement boundries
    if nutY <= 0:
        nutY = 0
    elif nutY >= 450:
        nutY = 450

    paperclipY += paperclipY_change
# paperclip movement boundries
    if paperclipY <= 0:
        paperclipY = 0
    elif paperclipY >= 450:
        paperclipY = 450

    bombY += bombY_change
# coin movement boundries
    if bombY <= 0:
        bombY = 0
    elif bombY >= 450:
        bombY = 450



    player(playerX, playerY)
    coin(coinX, coinY)
    paperclip(paperclipX, paperclipY)
    nut(nutX, nutY)
    bomb(bombX, bombY)
    pygame.display.update()
