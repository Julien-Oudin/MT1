import pygame
import sys
import datetime as dt
from Classes.Player import Player
from Classes.Platform import Platform
from Classes.Button import Button
from Classes.Door import Door
from Classes.Spikes import Spikes

# from Canon import Canon

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("More than 1")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)


# Death count

# Default keyboard settings

keys_user = {"left_key": pygame.K_q,
             "right_key": pygame.K_d,
             "dash_key": pygame.K_LSHIFT,
             "jump_key": pygame.K_SPACE,
             "enter_door_key": pygame.K_e}

# Initialisation of the state of the projectile
projectile_launched = False

# Environment properties
hour = dt.datetime.now().hour

# Create player object

player = Player(100, screen_height - 170, screen_height)

# Create groups of objects
# Starts by platforms

platforms = pygame.sprite.Group()

# Create secret platforms that appear when a button is pushed
platforms_S = pygame.sprite.Group()

# Create a button group and an array that will be used to see which are activated

buttons = pygame.sprite.Group()
buttons_arr_act = []

# Create a group of doors and put the door in it

doors = pygame.sprite.Group()

# Create a group of spikes and puts the first one in it
spikes_group = pygame.sprite.Group()


# Function to load level 1


def load_level_1():
    global player, platforms, platforms_S, buttons, doors, spikes_group, t_launch, buttons_arr_act
    player.spawn()
    platforms = pygame.sprite.Group()
    platform_1 = Platform(0, screen_height - 70, screen_width, 100)  # Ground
    platform_2 = Platform(200, 700, 200, 5)
    platform_3 = Platform(500, 800, 150, 5)
    platform_4 = Platform(875, 630, 100, 5)
    platforms.add(platform_1, platform_2, platform_3, platform_4)
    platforms_S = pygame.sprite.Group()
    platform_S_1 = Platform(650, 730, 50, 5)
    platforms_S.add(platform_S_1)
    buttons = pygame.sprite.Group()
    button0 = Button(250, 670, 20, 30, RED)
    buttons_arr_act = []
    buttons.add(button0)
    doors = pygame.sprite.Group()
    door1 = Door(900, 530)
    doors.add(door1)
    spikes_group = pygame.sprite.Group()
    spikes1 = Spikes(platform_4, 20, 30, 220, screen)
    spikes_group.add(spikes1)
    t_launch = pygame.time.get_ticks()


# Function to load level 2


def load_level_2():
    global player, platforms, platforms_S, buttons, doors, spikes_group, t_launch
    player.spawn()
    platforms = pygame.sprite.Group()
    platform_1 = Platform(0, screen_height - 70, screen_width, 100)
    platform_2 = Platform(300, 600, 200, 5)
    platform_3 = Platform(600, 700, 150, 5)
    platforms.add(platform_1, platform_2, platform_3)
    platforms_S = pygame.sprite.Group()
    platform_S_1 = Platform(750, 650, 50, 5)
    platforms_S.add(platform_S_1)
    buttons = pygame.sprite.Group()
    button0 = Button(350, 570, 20, 30, RED)
    buttons_arr_act.clear()
    buttons.add(button0)
    doors = pygame.sprite.Group()
    door1 = Door(900, 500)
    doors.add(door1)
    spikes_group = pygame.sprite.Group()
    spikes1 = Spikes(platform_3, 20, 30, 220, screen)
    spikes_group.add(spikes1)
    t_launch = pygame.time.get_ticks()

def load_level_3():
    global player, platforms, platforms_S, buttons, doors, spikes_group, t_launch
    player.spawn()
    platforms = pygame.sprite.Group()
    platform_1 = Platform(0, screen_height - 70, screen_width, 100)
    platform_2 = Platform(300, 600, 200, 5)
    platform_3 = Platform(600, 700, 150, 5)
    platform_4 = Platform(900, 600, 200, 5)
    platforms.add(platform_1, platform_2, platform_3,platform_4)
    platforms_S = pygame.sprite.Group()
    platform_S_1 = Platform(950, 380, 50, 5)
    platforms_S.add(platform_S_1)
    buttons = pygame.sprite.Group()
    button0 = Button(350, 570, 20, 30, RED)
    buttons_arr_act.clear()
    buttons.add(button0)
    doors = pygame.sprite.Group()
    door1 = Door(1200, 150)
    doors.add(door1)
    spikes_group = pygame.sprite.Group()
    spikes1 = Spikes(platform_3, 20, 30, 220, screen)
    spikes2 = Spikes(platform_S_1, 20, 30, 220, screen)

    spikes_group.add(spikes1,spikes2)
    t_launch = pygame.time.get_ticks()

def load_level_4():
    global player, platforms, platforms_S, buttons, doors, spikes_group, t_launch, buttons_arr_act
    player.spawn()
    platforms = pygame.sprite.Group()
    platform_1 = Platform(0, screen_height - 70, screen_width, 100)  # Ground
    platform_2 = Platform(200, 200, 100, 5)
    platform_3 = Platform(200, 400, 100, 5)
    platform_4 = Platform(200, 630, 100, 5)
    platforms.add(platform_1, platform_2, platform_3, platform_4)
    platforms_S = pygame.sprite.Group()
    platform_S_1 = Platform(800, 430, 100, 5)
    platforms_S.add(platform_S_1)
    buttons = pygame.sprite.Group()
    button0 = Button(250, 170, 20, 30, RED)
    buttons_arr_act = []
    buttons.add(button0)
    doors = pygame.sprite.Group()
    door1 = Door(1350, 330)
    doors.add(door1)
    t_launch = pygame.time.get_ticks()

def load_level_5():
    global player, platforms, platforms_S, buttons, doors, spikes_group, t_launch, buttons_arr_act
    player.spawn()
    reverse()
    platforms = pygame.sprite.Group()
    platform_1 = Platform(100, screen_height - 70, screen_width-200, 100)  #Ground
    platform_2 = Platform(200, 700, 200, 5)
    platform_4 = Platform(1000, 530, 200, 5)
    platforms.add(platform_1, platform_2, platform_4)
    platforms_S = pygame.sprite.Group()
    platform_S_1 = Platform(500, 500, 50, 5)
    platforms_S.add(platform_S_1)
    buttons = pygame.sprite.Group()
    button0 = Button(250, 670, 20, 30, RED)
    buttons_arr_act = []
    buttons.add(button0)
    doors = pygame.sprite.Group()
    door1 = Door(1100, 430)
    doors.add(door1)
    spikes_group = pygame.sprite.Group()
    spikes1 = Spikes(platform_4, 20, 30, 220, screen)
    spikes_group.add(spikes1)
    t_launch = pygame.time.get_ticks()

# List of levels


levels = [load_level_1, load_level_2,load_level_3,load_level_4,load_level_5]
current_level = 0

# Load the first level
levels[current_level]()


# Functions used in the game


def reverse():
    tmp = keys_user["right_key"]
    keys_user["right_key"] = keys_user["left_key"]
    keys_user["left_key"] = tmp
    tmp = keys_user["jump_key"]
    keys_user["jump_key"] = keys_user["dash_key"]
    keys_user["dash_key"] = tmp


clock = pygame.time.Clock()

# Module for writing initialization
pygame.font.init()
font_used = pygame.font.SysFont('Kanit', 30)
text = font_used.render('Press "E" to open the door', False, BLACK)

# Music module

music_loop = ["music\main_title1.mp3", "music\main_title2.mp3", "music\main_title3.mp3", "music\main_title4.mp3"]
music_state = 0
pygame.mixer.music.load(music_loop[music_state])
pygame.mixer.music.play()

# Main loop
running = True
t_launch = pygame.time.get_ticks()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t_act = pygame.time.get_ticks() - t_launch

    keys = pygame.key.get_pressed()
    if keys[keys_user["left_key"]]:
        player.rect.x -= player.speed
        player.orientation = "W"
    if keys[keys_user["right_key"]]:
        player.rect.x += player.speed
        player.orientation = "E"
    if keys[keys_user["dash_key"]]:
        player.dash()
    if keys[keys_user["jump_key"]]:
        player.jump()

    # Check for collisions with platforms
    collisions = pygame.sprite.spritecollide(player, platforms, False)
    for platform in collisions:
        if player.y_velocity > 0 and player.rect.bottom > platform.rect.top:
            player.rect.bottom = platform.rect.top
            player.on_ground = True
            player.y_velocity = 0

    for spike in spikes_group.sprites():
        if spike.activated(player.rect):
            spike.draw()
            if spike.rect.colliderect(player.rect):
                player.spawn()
                spike.t_activated = t_act
                spike.triggered = False

    i = 0
    for button in buttons:
        button.touch_player(player)
        buttons_arr_act.append(button.triggered)
        i += 1
    '''
    platforms_activated = 1
        # If buttons are pressed, the platforms spawn and it checks collisions
    for i in range(len(buttons_arr_act)):
        if buttons_arr_act[i] == 0:
            platforms_activated = 0
    '''
    for i in range(len(buttons_arr_act)):
        if buttons_arr_act[i]:
            collisions = pygame.sprite.spritecollide(player, platforms_S, False)
            for platform in collisions:
                if player.y_velocity > 0 and player.rect.bottom > platform.rect.top:
                    player.rect.bottom = platform.rect.top
                    player.on_ground = True
                    player.y_velocity = 0
            platforms_S.draw(screen)

    for door in doors:
        if door.rect.colliderect(player.rect):
            screen.blit(text, (player.rect.centerx - 125, player.rect.top - 120))
            if keys_user["enter_door_key"]:
                door.image = pygame.image.load("Images\Opened_Door.png")
                door.image = pygame.transform.scale(door.image, (100, 100))
                pygame.mixer_music.stop()
                pygame.mixer.music.load("music\win.mp3")
                pygame.mixer.music.play()
                music_state += 1
                current_level += 1
                if current_level < len(levels):
                    levels[current_level]()
                else:
                    ###################################################### END
                    running = False
    player.update()
    buttons.update()
    buttons.draw(screen)
    platforms.draw(screen)
    doors.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    if not pygame.mixer.music.get_busy():
        music_state += 1
        if music_state > 3:
            music_state = 0
        pygame.mixer.music.load(music_loop[music_state])
    clock.tick(60)
    if player.rect.y + player.rect.height >= screen_height:
        player.spawn()

pygame.quit()
sys.exit()
