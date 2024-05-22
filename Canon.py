import pygame


# Create a class that shoots projectiles to the player
class Canon(pygame.sprite.Sprite):

    def __init__(self, sub_platform, length, height, dis_trigger, screen_height):
        super().__init__()
        self.proj_size = 20
        self.speed = 1
        self.projectile_step = 0
        self.projectile_trajectory = []
        self.projectile_x = length
        self.projectile_y = screen_height // 2 - self.proj_size // 2
        self.projectile_step = 0
        self.projectile_trajectory = []