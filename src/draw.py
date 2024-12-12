import pygame
import Environment


def init_board(screen:pygame.display, rect_size):
    screen.fill("black")
    for i in range(screen.get_width()//rect_size):
        for j in range(screen.get_height()//rect_size):
            pygame.draw.rect(screen, "white", pygame.Rect(1+i*rect_size+i, 1+j*rect_size+j, rect_size, rect_size), border_radius=1)
            
def draw_board(screen:pygame.display, rect_size, env:Environment):
    screen.fill("black")
    for x in range(env.tailleX):
        for y in range(env.tailleY):
            if env.grilleTres[x][y]:
                pygame.draw.rect(screen, "red", pygame.Rect(1+x*rect_size+x, 1+y*rect_size+y, rect_size, rect_size), border_radius=1) 
            elif env.grilleAgent[x][y]:
                pygame.draw.rect(screen, "blue", pygame.Rect(1+x*rect_size+x, 1+y*rect_size+y, rect_size, rect_size), border_radius=1) 
            else:
                pygame.draw.rect(screen, "white", pygame.Rect(1+x*rect_size+x, 1+y*rect_size+y, rect_size, rect_size), border_radius=1) 