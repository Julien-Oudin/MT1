import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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

# Create player object
player = Player(100, screen_height - 70 - player_height)

# Create platform objects
platforms = pygame.sprite.Group()

platforms.add(Platform(0, screen_height - 70, screen_width, 100))
platforms.add(Platform(200, 700, 200, 5))
platforms.add(Platform(500, 800, 150, 5))
platforms.add(Platform(600, 650, 10, 10))

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

    player.update()
    if player.rect.y + player_height >= screen_height:
        running = False
    platforms.draw(screen)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()