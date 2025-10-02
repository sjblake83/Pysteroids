import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = {updatable, drawable}
    Asteroid.containers = {updatable, drawable, asteroids}
    AsteroidField.containers = {updatable}
    Shot.containers = {updatable, drawable}
    
    screen_midway_x = SCREEN_WIDTH / 2
    screen_midway_y = SCREEN_HEIGHT / 2
    player = Player(screen_midway_x, screen_midway_y)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collission(player):
                print("Game over!")
                return
        pygame.display.flip()
        dt = (clock.tick(60.0) / 1000)

if __name__ == "__main__":
    main()
