from config import loadFileConfig
from draw import draw_board
import pygame
from time import sleep
import random
horizon = 100




def main():
    pygame.init()
    rect_size = 50
    env, lAg = loadFileConfig("env1.txt")
    screen = pygame.display.set_mode((env.tailleX*rect_size+env.tailleX, env.tailleY*rect_size+env.tailleY))
    clock = pygame.time.Clock()
    
    
    draw_board(screen, rect_size, env)
    sleep(2)
    
    # env, lAg = loadFileConfig("env1.txt")
    print(env)
    for a in lAg.values() :
        print(a)

    print(vars(lAg.get("agent0")))
    #Exemple where the agents move and open a chest and pick up the treasure
    lAg.get("agent0").move(7,4,7,3)
    draw_board(screen, rect_size, env)
    sleep(2)
    lAg.get("agent0").move(7, 3, 6, 3)
    draw_board(screen, rect_size, env)
    sleep(2)
    lAg.get("agent0").open()
    draw_board(screen, rect_size, env)
    sleep(2)
    print(env)
    lAg.get("agent0").move(6, 3, 7, 3)
    draw_board(screen, rect_size, env)
    sleep(2)
    print(env)
    lAg.get("agent4").move(6,7,6,6)
    lAg.get("agent4").move(6, 6, 6, 5)
    lAg.get("agent4").move(6, 5, 6, 4)
    lAg.get("agent4").move(6, 4, 6, 3)
    print(env)
    lAg.get("agent4").load(env) # fail because agent4 has not the right type
    lAg.get("agent4").move(6, 3, 7, 5) # fail because position (7,5) is not a neighbour of the current position
    lAg.get("agent4").move(6, 3, 6, 2)
    print(env)
    lAg.get("agent2").move(5, 2, 5, 3)
    lAg.get("agent2").move(5, 3, 6, 3)
    lAg.get("agent2").load(env) # Success !
    print(env)

    # env.gen_new_treasures(5, 7)
    print(env)

    #Example of unload tresor
    lAg.get("agent2").move(6, 3, 5,2)
    lAg.get("agent2").move(5, 2, 5, 1)
    lAg.get("agent2").move(5, 1, 5, 0)
    lAg.get("agent2").unload()
    print(env)
    #  Example where the agents communicate

    lAg.get("agent2").send("agent4", "Hello !")
    lAg.get("agent4").readMail()

    ##############################################
    ####### TODO #################################
    ##############################################
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # draw_board(screen, rect_size, env)
        # pygame.display.flip()


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