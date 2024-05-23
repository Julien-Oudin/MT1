import pygame


# Class that creates spikes that makes the player respawn, they are only active when the player is close to the spikes
class Spikes(pygame.sprite.Sprite):
    def __init__(self, sub_platform, length, height, dis_trigger, screen):
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
        self.screen = screen

        # Here the rectangle is for the whole set of spikes

    def activated(self, rect_player):
        if self.rect_trigger.colliderect(rect_player) or self.triggered:
            if not self.triggered:
                self.triggered = True
                self.t_activated = pygame.time.get_ticks()
            else:
                if (pygame.time.get_ticks()) - self.t_activated >= self.t_activation:
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
            pygame.draw.polygon(self.screen, (35, 35, 35), spike_corners)