import pygame
import sys
from constants import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Sets game window height + width
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt: float = 0.0 #Delta time variable

    #GAME LOOP
    while True:
        log_state()#Magic black box

        for event in pygame.event.get(): #Constant check for inputs
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        #Asteroid collision checks
        for asteroid in asteroids:
            #Checks for collision with player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            #Checks for collision with any shot
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black") #Sets the screen color

        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip() #Refreshes display/window

        dt = clock.tick(60) / 1000 #Limits FPS to 60


if __name__ == "__main__":
    main()
