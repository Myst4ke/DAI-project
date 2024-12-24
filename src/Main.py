from config import loadFileConfig, loadMoveSet
from draw import draw_board
import pygame
from time import sleep
import random
horizon = 100
rect_size = 50
FPS = 1
clock = pygame.time.Clock()
SCROLL_SPEED = 0.5

def main():
    global FPS
    pygame.init()
    env, lAg = loadFileConfig("env1.txt")
    screen = pygame.display.set_mode((env.tailleX*rect_size+env.tailleX, env.tailleY*rect_size+env.tailleY))
    moves = loadMoveSet("moves.txt", env, lAg)
    
    draw_board(screen, rect_size, env)
    sleep(2)
    
    running = True
    pause = False
    while running:
        clock.tick(FPS)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
                print("paused" if pause else "unpaused")   
            if event.type == pygame.MOUSEWHEEL:
                # Increase or decrease FPS based on scroll direction
                FPS = max(1, FPS + (event.y * SCROLL_SPEED))
                print(f"FPS: {FPS}")
                        
        if not pause:
            next(moves)()
            draw_board(screen, rect_size, env)
        
    
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