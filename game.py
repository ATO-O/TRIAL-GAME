import pygame
import random

# initializing pygame
pygame.init()

# setting screen
screen = pygame.display.set_mode((1000, 600))
running = True
spawn_timer = 0
spawn_rate = 60
game_time = 0

# display text & icons
pygame.display.set_caption("Magnatiz")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# player icon
playerImg = pygame.image.load("player.png")
playerX = 450
playerY = 480
playerX_change = 0

# magnet force
lightImg = pygame.image.load("lightning.png")
lightX = 0
lightY = 50
light_state = "OFF"


def player(x, y):
    screen.blit(playerImg, (x, y))


def light(x, y):
    global light_state
    light_state = "ON"
    screen.blit(lightImg, (x + 45, y+10))


# obstacles and collectible functions
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = 2

    def update(self):
        self.y += self.velocity_y

    def draw(self, screen):
        pass  # Override in child classes

    def boundries(self):
        if self.y >= 600:  # Changed from 450 to 600 (screen height)
            self.y = 0
            self.x = random.randint(0, 870)  # Fixed typo: randit -> randint


class Coin(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 10
        self.image = pygame.image.load("silver-badge.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class paperclip(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 5
        self.image = pygame.image.load("paperclip.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bomb(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.deadly = True
        self.image = pygame.image.load("bomb.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Screw(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.points = 5
        self.image = pygame.image.load("nut.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Now add them all to ONE list
objects = []
objects.append(Coin(0, 50))
objects.append(paperclip(200, 50))
objects.append(Bomb(400, 50))
objects.append(Screw(600, 50))

# background icon
background = pygame.image.load("background.png")

# game loop
while running:
    # rgb - theme of screen
    screen.fill((0, 0, 255))
    # background image
    screen.blit(background, (0, 0))

#loop for checking clicking or keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keystroke movevent for the player.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                light_state = "ON"  # Just set state
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                light_state = "OFF"  # Turn off when released
    #spawning multiple collectibles
    spawn_timer += 1 #increase timer every frame
    if spawn_timer >= spawn_rate:
        #time to spawn pick random position
        random_x = random.randint(50, 900)

        #pick random object type
        choice = random.randint(1, 4)
        if choice == 1:
            objects.append(Coin(random_x, 0))
        elif choice == 2:
            objects.append(Screw(random_x, 0))
        elif choice == 3:
            objects.append(paperclip(random_x, 0))
        elif choice == 4:
            objects.append(Bomb(random_x, 0))

        spawn_timer = 0  #reset the timer

    #difficulty loop
    game_time += 1

    #adjusting diffuculty
    if game_time < 1800:
        spawn_rate = 60
    elif game_time >= 3600:
        spawn_rate = 45
    else:
        spawn_rate = 30


    playerX += playerX_change
    # player movement boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 870:
        playerX = 870

    # Update and draw all objects (MOVED INSIDE LOOP!)
    for obj in objects:
        obj.update()
        obj.boundries()
        obj.draw(screen)

        #remove if off screen
        if obj.y >= 650:
            objects.remove(obj)

    # Draw lightning effect if active
    if light_state == "ON":
        light(playerX, playerY)

    player(playerX, playerY)
    pygame.display.update()
