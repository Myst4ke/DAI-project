import pygame
from Environment import Environment
from MyAgent import MyAgent
from MyAgentGold import  MyAgentGold
from MyAgentChest import MyAgentChest
from MyAgentStones import MyAgentStones
from Treasure import Treasure

COLORS = {
    "yellow": (252, 220, 56),
    "blue": (33, 148, 255),
    "red": (204, 8, 44),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "green": (0, 255, 0)
}

TYPE_COLORS = {
    1: COLORS["yellow"],  # Gold treasure
    2: COLORS["red"],     # Stone treasure
    MyAgentGold: COLORS["yellow"],
    MyAgentStones: COLORS["red"],
    MyAgentChest: COLORS["blue"]
}

def _get_cell_rect(x: int, y: int, rect_size) -> pygame.Rect:
        """ Helper method to calculate cell rectangle """
        return pygame.Rect(
            1 + y * (rect_size + 1),
            1 + x * (rect_size + 1),
            rect_size,
            rect_size
        )


def _draw_text(screen:pygame.display, text: str, rect: pygame.Rect, color="black"):
        """ Helper method to draw centered text """
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(text), True, COLORS[color])
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)


def _draw_treasure(screen:pygame.display, rect_size, x, y, treasure:Treasure): 
    """ Draw a treasure as a colored square (color depends on treasure type) """
    pygame.draw.rect(screen, TYPE_COLORS[treasure.type], my_rect:= _get_cell_rect(x, y, rect_size))
    
    if treasure.opened: # Draws green borders if opened
        pygame.draw.rect(screen, "green", my_rect, width=3)
    _draw_text(screen, str(treasure.value), my_rect)


def _draw_agent(screen:pygame.display, rect_size, x, y, agent:MyAgent):
    """ Draw an agent as a colored circle (color depends on agent type) """
    my_rect = _get_cell_rect(x, y, rect_size)
    circle_center = (my_rect.centerx, my_rect.centery)
    radius = (rect_size - 2) // 2
    
    pygame.draw.circle(screen, TYPE_COLORS[type(agent)], circle_center, radius)
    pygame.draw.circle(screen, COLORS["black"], circle_center, radius, 3)
    _draw_text(screen, str(agent.getCapacity()-agent.getTreasure()), my_rect)


def _draw_depot(screen:pygame.display, rect_size, env:Environment):
    """ Draws the depot zone in green"""
    pygame.draw.rect(screen, "GREEN", my_rect:=_get_cell_rect(*env.posUnload, rect_size))
    _draw_text(screen, "D", my_rect)



def draw_emptyCell(screen:pygame.display, rect_size:int, x:int, y:int):
    """ Draws a empty cell """
    pygame.draw.rect(screen, "white", _get_cell_rect(x,y, rect_size))


def draw_cell(screen:pygame.display, env:Environment, rect_size, x, y):
    """ Draws agents and treasures """
    if env.posUnload != (x,y):
        draw_emptyCell(screen, rect_size, x, y)
    
    if treasure:=env.grilleTres[x][y]:
        _draw_treasure(screen, rect_size, x, y, treasure)
    if agent:=env.grilleAgent[x][y]:
        _draw_agent(screen, rect_size, x, y, agent)


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
    pygame.display.flip()        