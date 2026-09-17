import pygame
from pygame import Surface


class Animation:
    FRAME_DURATION: int = 100

    screen: Surface
    images: list
    x: int
    y: int
    start_time: int
    is_started: bool
    is_finished: bool

    def __init__(self, screen, images, x, y):
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
        self.start_time = 0
        self.is_started = False
        self.is_finished = False

    def play(self, current_time: int):
        if not self.is_started:
            self.start_time = current_time
            self.is_started = True

        temps_ecoule: int = current_time - self.start_time
        frame_index: int = temps_ecoule // Animation.FRAME_DURATION

        if frame_index < len(self.images):
            self.screen.blit(self.images[frame_index], (self.x, self.y))
            pygame.display.update()
        else:
            self.is_finished = True
