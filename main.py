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

# Menu function
def show_menu():
    screen.fill((0, 0, 0))
    title_font = pygame.font.SysFont("Comic Sans MS", 50)
    option_font = pygame.font.SysFont("Comic Sans MS", 30)
    
    title_text = title_font.render("Asteroid Game", True, (255, 255, 255))
    easy_text = option_font.render("1. Easy", True, (225, 225, 225))
    medium_text = option_font.render("2. Medium", True, (255, 255, 255))
    hard_text = option_font.render("3. Hard", True, (255, 255, 255))
    
    screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))
    screen.blit(easy_text, (SCREEN_WIDTH//2 - easy_text.get_width()//2, 200))
    screen.blit(medium_text, (SCREEN_WIDTH//2 - medium_text.get_width()//2, 250))
    screen.blit(hard_text, (SCREEN_WIDTH//2 - hard_text.get_width()//2, 300))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "medium"
                elif event.key == pygame.K_3:
                    return "hard"

# Game over function
def show_game_over(score):
    screen.fill((0, 0, 0))
    title_font = pygame.font.SysFont("Comic Sans MS", 50)
    option_font = pygame.font.SysFont("Comic Sans MS", 30)

    title_text = title_font.render("Game Over!", True, (255, 0, 0))
    score_text = option_font.render(f"Your Score: {int(score)}", True, (255, 255, 255))
    restart_text = option_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

    screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))
    screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 200))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 300))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return False
    


#defining the main function
def game_loop():
    global ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN
    
    while True:
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()
        
        score = 0
        difficulty = show_menu()
        if difficulty is None:
            return
        
        ASTEROID_SPAWN_RATE, PLAYER_SHOT_COOLDOWN = get_difficulty_settings(difficulty)
        AsteroidField(ASTEROID_SPAWN_RATE)
        
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SHOT_COOLDOWN)
        updatable.add(player)
        drawable.add(player)
    
    
    
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
                        if not show_game_over(score):
                            return # Exit game if player chooses not to start
                        return game_loop() # Restart the game if the player chooses to play again

            screen.fill((0, 0, 0))
            for obj in drawable:
                obj.draw(screen)

            screen.blit(textsurface, (0, 0))
            pygame.display.flip()


if __name__ == "__main__":
    game_loop()