import pygame


# New class that creates a door, the objective of each level
class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images\Closed_door.png")
        self.image = pygame.transform.scale(self.image, (40, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
