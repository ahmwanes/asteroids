import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        # check if the user has closed the window, and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User Quit!")
                return

        screen.fill(color="black")

        updatable.update(dt)

        for obj in asteroids:
            colleded = obj.collides_with(player)
            if colleded:
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
