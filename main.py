import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        screen.fill("black")
        for unit in drawable:
            unit.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        # fps = 60
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()