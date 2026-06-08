import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    running = True

    while running:
        log_state()
        dt = clock.tick(60) / 1000  # limits FPS to 60 and calculates delta time
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
    # UPDATE YOUR GAME HERE & RENDER YOUR GAME HERE
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
    # flip() the display to put your work on screen
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
