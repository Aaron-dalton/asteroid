#importing important stuff
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#creating two main groups for updateable objects and drawable objects
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = updatable, drawable
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)
clock = pygame.time.Clock()


#defining the main function
def __main__():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") #output for user
    

    AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #initizalizing the screen loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (clock.tick(60) / 1000)
        
        updatable.update(dt)
        for obj in asteroids:
            for shot in shots:
                if shot.collisions(obj):
                    shot.kill()
                    obj.split()
                    break
            if player.collisions(obj):
                print("Game Over!")
                return

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()


if __name__ == "__main__":
    __main__() 