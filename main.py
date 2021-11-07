import sys
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

black_side_color = (255, 255, 255)
white_side_color = (0, 0, 0)

square_size = 75

screen_width = square_size * 8
screen_height = square_size * 8


screen = pygame.display.set_mode((screen_width, screen_height))

# build chessboard
for x in range(1, 9):
    for y in range(1, 9):
        if x % 2 == 1:
            if y % 2 == 1:
                color = black_side_color
            else:
                color = white_side_color
        else:
            if y % 2 == 1:
                color = white_side_color
            else:
                color = black_side_color
        pygame.draw.rect(screen, color, pygame.Rect(
            (x - 1) * square_size, (y - 1) * square_size, square_size, square_size))

pygame.display.flip()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEWHEEL:
                pygame.display.flip()
        clock.tick(60)


# Execute game:
main()
