import pygame
from Environment import Environment
from MyAgentGold import  MyAgentGold
from MyAgentChest import MyAgentChest
from MyAgentStones import MyAgentStones
from Treasure import Treasure
from time import sleep


def init_board(screen:pygame.display, rect_size):
    screen.fill("black")
    for i in range(screen.get_width()//rect_size):
        for j in range(screen.get_height()//rect_size):
            pygame.draw.rect(screen, "white", pygame.Rect(1+i*rect_size+i, 1+j*rect_size+j, rect_size, rect_size), border_radius=1)
            
def draw_board(screen:pygame.display, rect_size, env:Environment):
    screen.fill("black")
    # Police de caractères
    font = pygame.font.Font(None, 36)
    typeColorDict= {
        1:"yellow",
        2:'red',
        MyAgentGold: "yellow",
        MyAgentStones: "red",
        MyAgentChest: "blue"
    }
    
    for x in range(env.tailleX):
        for y in range(env.tailleY):
            if treasure:=env.grilleTres[x][y]:
                pygame.draw.rect(screen, typeColorDict[treasure.type], my_rect:=pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size))
                
                text = font.render(str(treasure.value), True, "black")
                text_rect = text.get_rect(center=my_rect.center)
                screen.blit(text, text_rect) 
            elif agent:=env.grilleAgent[x][y]:
                pygame.draw.rect(screen, "white", my_rect:=pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size))
                pygame.draw.circle(screen, typeColorDict[type(agent)], (1+y*rect_size+y+(rect_size//2), 1+x*rect_size+x+(rect_size//2)), (rect_size-2)/2)
                pygame.draw.circle(screen, "black", (1+y*rect_size+y+(rect_size//2), 1+x*rect_size+x+(rect_size//2)), (rect_size-2)/2,3)
                
                text = font.render(str(agent.getCapacity()), True, "black")
                text_rect = text.get_rect(center=my_rect.center)
                screen.blit(text, text_rect) 
            else:
                pygame.draw.rect(screen, "white", pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size)) 

    depot_x, depot_y = env.posUnload
    depot_rect = pygame.Rect(1+depot_y * rect_size+depot_y, 1+depot_x * rect_size+depot_x, rect_size, rect_size)
    pygame.draw.rect(screen, "GREEN", depot_rect)
    pygame.display.flip()
    sleep(2)