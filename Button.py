import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Class that creates a button
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
