from config import loadFileConfig, loadMoveSet
from draw import draw_board
import pygame
from time import sleep
import random
horizon = 100
rect_size = 70
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
    
    t = 1
    while running and t < horizon:
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
            for a in lAg.values():
                a.optiPolicy()
            
            draw_board(screen, rect_size, env) 
            # next(moves)()
            
            if(t%10 == 0):
                env.gen_new_treasures(random.randint(0,5), 7)
            t+=1
    
    pygame.quit()
    moyMove = 0
    for a in lAg.values():
        moyMove += a.nbMove
    with open('data/optiMargin2.csv', "a") as f:
        f.write(f"\n{env.getScore()[0]},{env.getScore()[1]},{round(moyMove/len(lAg.values()))}")
        
    print(f"\n{env.getScore()[0]},{env.getScore()[1]},{round(moyMove/len(lAg.values()))}")
    
    
if __name__ == "__main__":
    main()