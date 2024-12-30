import pygame
from constants import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock
    dt = 0
    while True:
        Clock.tick(60)
        dt = Clock.get_time()/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()