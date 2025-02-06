#importing important stuff
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from settings import get_difficulty_settings

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
myfont = pygame.font.SysFont("Comic Sans MS", 30)


#defining the main function
def __main__():
    global ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN
    score = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") #output for user
    difficulty = input("Enter difficulty (easy, medium, hard): ")

    ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN = get_difficulty_settings(difficulty)
    print(f"Asteroid spawn rate: {ASTEROID_SPAWN_RATE}, player shot cooldown: {PLAYER_SHOT_COOLDOWN}")
    AsteroidField(ASTEROID_SPAWN_RATE)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SHOT_COOLDOWN)
    updatable.add(player)
    drawable.add(player)
    #initizalizing the screen loop
    while True: 
        textsurface = myfont.render(f"Score {int(score)}", False, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (clock.tick(60) / 1000)
        score += dt
        updatable.update(dt)
        for obj in asteroids:
            for shot in shots:
                if shot.collisions(obj):
                    score += 10
                    shot.kill()
                    obj.split()
                    break
            if player.collisions(obj):
                print("Game Over!")
                print(f"Your score was: {int(score)}")
                return

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        screen.blit(textsurface, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    __main__() 