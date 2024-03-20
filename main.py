import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hooked On This")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_width = 50
player_height = 50
player_color = BLACK
jump_strength = -12
gravity = 0.5

# Platform properties
platform_color = BLUE

# Create player class


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_velocity = 0
        self.on_ground = False

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
                self.height /= 3
                # Resize the button's image
                self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
                self.last_pressed = pygame.time.get_ticks()

    def reset_image(self):
        if self.triggered:
            if self.timed(pygame.time.get_ticks()):
                self.last_pressed = None
                self.triggered = False
                self.image = self.original_image
                self.rect = self.original_rect
                self.height = self.original_height
                self.rect.x = self.original_x

    def timed(self, time):
        if time - self.last_pressed >= 2000:
            return True


# Create player object


player = Player(100, screen_height - 70 - player_height)


# Create platform objects
platforms = pygame.sprite.Group()
platform1 = Platform(0, screen_height - 70, screen_width, 100)
platform2 = Platform(200, 700, 200, 5)
platform3 = Platform(500, 800, 150, 5)
platform4 = Platform(500, 800, 150, 5)
platforms.add(platform1, platform2, platform3, platform4)


# Create a button group and put the first button in
buttons = pygame.sprite.Group()
button0 = Button(250, 670, 20, 30, RED)
buttons.add(button0)

# Main loop
clock = pygame.time.Clock()

running = True
t_launch = pygame.time.get_ticks()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    # Check for collisions with platforms
    collisions = pygame.sprite.spritecollide(player, platforms, False)
    for platform in collisions:
        if player.y_velocity > 0 and player.rect.bottom > platform.rect.top:
            player.rect.bottom = platform.rect.top
            player.on_ground = True
            player.y_velocity = 0

    t_act = t_launch - pygame.time.get_ticks()
    platforms.sprites()[0].rect.x -= t_act / 1000
    platforms.sprites()[0].rect.width -= t_act / 1000

    button0.touch_player(player)
    player.update()
    button0.update()
    if player.rect.y + player_height >= screen_height:
        running = False
    platforms.draw(screen)
    buttons.draw(screen)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
