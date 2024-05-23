import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Class that creates a button
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.original_image = pygame.image.load("Images\Button_disabled.png")
        self.original_image = pygame.transform.scale(self.original_image, (width+10, height+10))
        self.image = self.original_image.copy()
        self.image_enabled = pygame.image.load("Images\Button_enabled.png")
        self.image_enabled = pygame.transform.scale(self.image_enabled, (width+10, height+10))
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
            self.image = self.image_enabled  # Change the button's sprite
        else:
            self.image = self.image_enabled  # Change the button's sprite back

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
