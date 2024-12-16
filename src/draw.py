import pygame
from Environment import Environment
from MyAgent import MyAgent
from MyAgentGold import  MyAgentGold
from MyAgentChest import MyAgentChest
from MyAgentStones import MyAgentStones

yellow = (252, 220, 56)
blue = (33, 148, 255)
red = (204, 8, 44)

typeColorDict= {
    1: yellow,
    2: red,
    MyAgentGold: yellow,
    MyAgentStones: red,
    MyAgentChest: blue
}

def _draw_treasure(screen:pygame.display, rect_size, x, y, treasure): 
    """ Draw a treasure as a colored square (color depends on treasure type) """
    font = pygame.font.Font(None, 36)
    pygame.draw.rect(screen, typeColorDict[treasure.type], my_rect:=pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size))
    if treasure.opened:
        pygame.draw.rect(screen, "green", my_rect:=pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size), width=2)
    text = font.render(str(treasure.value), True, "black")
    text_rect = text.get_rect(center=my_rect.center)
    screen.blit(text, text_rect)

def _draw_agent(screen:pygame.display, rect_size, x, y, agent:MyAgent):
    """ Draw a agent as a colored circle (color depends on agent type) """
    font = pygame.font.Font(None, 36)
    my_rect = pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size)
    pygame.draw.circle(screen, typeColorDict[type(agent)], (1+y*rect_size+y+(rect_size//2), 1+x*rect_size+x+(rect_size//2)), (rect_size-2)/2)
    pygame.draw.circle(screen, "black", (1+y*rect_size+y+(rect_size//2), 1+x*rect_size+x+(rect_size//2)), (rect_size-2)/2,3)
    
    text = font.render(str(agent.getCapacity()-agent.getTreasure()), True, "black")#Prints the available capacity on the agent
    text_rect = text.get_rect(center=my_rect.center)
    screen.blit(text, text_rect)

def _draw_depot(screen:pygame.display, rect_size, env:Environment):
    """ Draws the depot zone in green"""
    font = pygame.font.Font(None, 36)
    depot_x, depot_y = env.posUnload
    pygame.draw.rect(screen, "GREEN", my_rect:=pygame.Rect(1+depot_y * rect_size+depot_y, 1+depot_x * rect_size+depot_x, rect_size, rect_size))
    text = font.render("D", True, "black")
    text_rect = text.get_rect(center=my_rect.center)
    screen.blit(text, text_rect) 
    
    pygame.display.flip()


def draw_emptyCell(screen:pygame.display, rect_size:int, x:int, y:int):
    """ Draws a empty cell """
    pygame.draw.rect(screen, "white", pygame.Rect(1+y*rect_size+y, 1+x*rect_size+x, rect_size, rect_size))
    pygame.display.flip()

def draw_cell(screen:pygame.display, env:Environment, rect_size, x, y):
    """ Draws agents and treasures """
    draw_emptyCell(screen, rect_size, x, y)
    
    if treasure:=env.grilleTres[x][y]:
        _draw_treasure(screen, rect_size, x, y, treasure)
    if agent:=env.grilleAgent[x][y]:
        _draw_agent(screen, rect_size, x, y, agent)
            
    pygame.display.flip()


def init_board(screen:pygame.display, rect_size):
    """ Draws the entire empty grid  """
    screen.fill("black")
    for x in range(screen.get_width()//rect_size):
        for y in range(screen.get_height()//rect_size):
            draw_emptyCell(screen, rect_size, x, y)
            
    pygame.display.flip()
  
def draw_board(screen:pygame.display, rect_size, env:Environment):
    """ Draws the entire board using `draw_cell` and `draw_depot` """
    screen.fill("black")
    _draw_depot(screen, rect_size, env)
    for x in range(env.tailleX):
        for y in range(env.tailleY):
            draw_cell(screen, env, rect_size, x, y)
            
    
    # sleep(2)