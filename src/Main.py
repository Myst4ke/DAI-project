from config import loadFileConfig, loadMoveSet
from draw import draw_board
import pygame
from time import sleep
import random
horizon = 100
rect_size = 50


def main():
    pygame.init()
    env, lAg = loadFileConfig("env1.txt")
    screen = pygame.display.set_mode((env.tailleX*rect_size+env.tailleX, env.tailleY*rect_size+env.tailleY))
    
    moves = loadMoveSet("moves.txt", env, lAg)
    
    draw_board(screen, rect_size, env)
    sleep(2)
    
    cpt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if cpt < len(moves):
            method, args = moves[cpt]
            method(*args)
                
            draw_board(screen, rect_size, env)
            sleep(1)   
            cpt+=1  
        else:
            running = False

    pygame.quit()

    # make the agents plan their actions (off-line phase) TO COMPLETE


    # make the agents execute their plans
    # for t in range(horizon):
    #     if(t%10 == 0):
    #         env.gen_new_treasures(random.randint(0,5), 7)
    #     for a in lAg.values():
    #         print(a)
            #here the action of agent a at timestep t should be executed

    # print each agent's score

    # print(env.grilleAgent)
    print(f"\n\n******* SCORE TOTAL : {env.getScore()}")

if __name__ == "__main__":
    main()