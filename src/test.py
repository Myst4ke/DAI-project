# Example file showing a circle moving on screen
import pygame
from draw import init_board, draw_board
from Main import loadFileConfig
import Environment

# pygame setup
pygame.init()
rect_size = 50
env, lAg = loadFileConfig("env1.txt")
screen = pygame.display.set_mode((env.tailleX*rect_size+env.tailleX, env.tailleY*rect_size+env.tailleY))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

print(env)
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    draw_board(screen, rect_size, env)
    # pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()