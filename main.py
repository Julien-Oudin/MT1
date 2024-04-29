import pygame
import sys
import datetime as dt

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

# Default keyboard settings

keys_user = {"left_key": pygame.K_q,
             "right_key": pygame.K_d,
             "dash_key": pygame.K_LSHIFT,
             "jump_key": pygame.K_SPACE,
             "enter_door_key": pygame.K_e}

# Player properties
player_width = 50
player_height = 50
player_color = BLACK
jump_strength = -12
gravity = 0.5

# Platform properties
platform_color = BLUE

# Door properties
door_color = BROWN

# Environment properties
hour = dt.datetime.now().hour

# Create player class


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.spawn_x = x
        self.rect.y = self.spawn_y = y
        self.speed = 5
        self.y_velocity = 0
        self.on_ground = False
        self.orientation = "E"
        self.last_dash = 0
        self.mini_dash = 0

    def spawn(self):
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y

    def update(self):
        self.y_velocity += gravity
        self.rect.y += self.y_velocity

        # Check if the player falls off the screen
        if self.rect.y > screen_height:
            pygame.quit()
            sys.exit()

        if self.rect.y >= screen_height - player_height:
            self.rect.y = screen_height - player_height
            self.on_ground = True
            self.y_velocity = 0

    def jump(self):
        if self.on_ground:
            self.y_velocity = jump_strength
            self.on_ground = False

    def dash(self):
        if pygame.time.get_ticks() - self.last_dash >= 1500:
            if self.orientation == "E":
                self.rect.x += 15
            elif self.orientation == "W":
                self.rect.x -= 15
            self.mini_dash += 1
            if self.mini_dash == 10:
                self.last_dash = pygame.time.get_ticks()
        else:
            self.mini_dash = 0

# Create platform class


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(platform_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Creating class Button


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.original_image = pygame.Surface((width, height))
        self.original_image.fill(color)
        self.image = self.original_image.copy()
        self.original_rect = self.image.get_rect(topleft=(x, y))
        self.rect = self.original_rect.copy()
        self.original_x = x
        self.original_height = height
        self.width = width
        self.height = height
        self.triggered = False
        self.last_pressed = None
        self.t_activation = 5000

    def update(self):
        self.reset_image()

        if self.triggered:
            self.image.fill(GREEN)  # Change the button's color to red when triggered
        else:
            self.image.fill(RED)  # Change the button's color to green when not triggered

    def touch_player(self, character):
        if not self.triggered:
            if self.rect.colliderect(character.rect):
                self.triggered = True
                self.rect.y += self.height * 2/3
                self.height //= 3
                # Resize the button's image
                self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
                self.last_pressed = pygame.time.get_ticks()

    def reset_image(self):
        if self.triggered:
            if self.timed(pygame.time.get_ticks()):
                self.last_pressed = None
                self.triggered = False
                self.height *= 3
                self.rect.y -= self.height * 2/3
                # Resize the button's image back
                self.image = pygame.transform.scale(self.original_image, (self.width, self.height))

    def timed(self, time):
        if time - self.last_pressed >= self.t_activation:
            return True
        return False

# Create class Door that is the goal of the level


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(door_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Create a spikes class, each object will be linked to a platform


class Spikes(pygame.sprite.Sprite):
    def __init__(self, sub_platform, length, height, dis_trigger):
        super().__init__()
        self.sub_platform = sub_platform
        self.height = height
        self.length_spike = length
        self.dis_trigger = dis_trigger
        self.border_distance = (self.sub_platform.rect.width % self.length_spike)
        self.rect = pygame.Rect(self.sub_platform.rect.x,
                                self.sub_platform.rect.y - self.height,
                                self.sub_platform.rect.width - self.border_distance,
                                self.height)
        self.rect_trigger = pygame.Rect(self.rect.x - self.dis_trigger,
                                        self.sub_platform.rect.y - self.dis_trigger,
                                        self.sub_platform.rect.width + self.dis_trigger * 1.5,
                                        self.height + self.dis_trigger)
        self.nb_spikes = self.sub_platform.rect.width // self.length_spike
        self.t_activated = 0
        self.t_activation = 5000
        self.triggered = False

        # Here the rectangle is for the whole set of spikes

    def activated(self, rect_player):
        if self.rect_trigger.colliderect(rect_player) or self.triggered:
            if not self.triggered:
                self.triggered = True
                self.t_activated = pygame.time.get_ticks() - t_launch
            else:
                if (pygame.time.get_ticks() - t_launch) - self.t_activated >= self.t_activation:
                    return False
            return True

    def draw(self):
        for i in range(self.nb_spikes):
            # In order : Top, left, right
            spike_corners = [(self.rect.x + ((i+0.5)*self.length_spike) + self.border_distance / 2,
                              self.rect.y - self.height),
                             ((self.rect.x + (i * self.length_spike)) + self.border_distance / 2,
                              self.sub_platform.rect.y + 1),
                             (self.rect.x + ((i+1)*self.length_spike) + self.border_distance/2,
                              self.sub_platform.rect.y + 1)]
            pygame.draw.polygon(screen, GRAY, spike_corners)


# Create player object


player = Player(100, screen_height - 70 - player_height)


# Create platform objects
platforms = pygame.sprite.Group()
platform_1 = Platform(0, screen_height - 70, screen_width, 100)
platform_2 = Platform(200, 700, 200, 5)
platform_3 = Platform(500, 800, 150, 5)
platform_5 = Platform(875, 630, 100, 5)

platforms.add(platform_1, platform_2, platform_3, platform_5)

# Create secret platforms that appear when a button is pushed
platforms_S = pygame.sprite.Group()
platform_S_1 = Platform(650, 730, 50, 5)

platforms_S.add(platform_S_1)

# Create a button group and put the first button in
buttons = pygame.sprite.Group()
button0 = Button(250, 670, 20, 30, RED)
buttons.add(button0)

# Create a group of doors and put the door in it
doors = pygame.sprite.Group()
door1 = (Door(900, 530, 50, 100))
doors.add(door1)

# Create a group of spikes and puts the first one in it
spikes_group = pygame.sprite.Group()
spikes1 = Spikes(platform_5, 20, 30, 220)
spikes_group.add(spikes1)

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

    button0.touch_player(player)
    # If button is pressed, the platforms spawn and it checks collisions
    if button0.triggered:
        collisions = pygame.sprite.spritecollide(player, platforms_S, False)
        for platform in collisions:
            if player.y_velocity > 0 and player.rect.bottom > platform.rect.top:
                player.rect.bottom = platform.rect.top
                player.on_ground = True
                player.y_velocity = 0
        platforms_S.draw(screen)

    if door1.rect.colliderect(player.rect):
        screen.blit(text, (player.rect.centerx - 125, player.rect.top - 120))
    # if keys_user["enter_door_key"]:
        # to Replace with the level change

    player.update()
    button0.update()
    buttons.draw(screen)
    platforms.draw(screen)
    doors.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
    if player.rect.y + player_height >= screen_height:
        running = False

pygame.quit()
sys.exit()
