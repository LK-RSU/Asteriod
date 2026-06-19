import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    # AsteroidField only needs to update to run its spawning timer
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    running = True

    while running:
        log_state()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # UPDATE YOUR GAME HERE & RENDER YOUR GAME HERE
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                # log, print, and exit here
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    # spawn fragments before removing the asteroid
                    try:
                        asteroid.kill()
                    except Exception:
                        pass
                    asteroid.split()
    # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
    # flip() the display to put your work on screen
        pygame.display.flip()
    # limits FPS to 60 and calculates delta time
        dt = clock.tick(60) / 1000  
    pygame.quit()


if __name__ == "__main__":
    main()
