from Environment import Environment
from MyAgentGold import  MyAgentGold
from MyAgentChest import MyAgentChest
from MyAgentStones import MyAgentStones
from Treasure import Treasure
import random
import re
horizon = 100

def startsWith(input:list, patern:str) -> bool:
    """ Return True if input list starts with patern else False """
    return True if input[0] == patern else False

def id_generator(start:int = 0):
    """ Yields id as 'angentN' """
    while True:
        yield f'agent{start}'
        start += 1

def loadFileConfig(nameFile) :
    with open(nameFile, 'r') as f:
        content = f.read()
    
    envConfigPattern = r'(\d+)\s+(\d+)'
    treasurePattern = r'(tres):(or|pierres):(\d+):(\d+):(\d+)'
    agentPattern = r'(AG):(ouvr|pierres|or):(\d+):(\d+)(?::(\d+))?'
    patterns = re.compile(fr'^(?!#){envConfigPattern}|{treasurePattern}|{agentPattern}', re.MULTILINE)
    matches = patterns.findall(content)
    
    matches = [[group for group in match if group != ''] for match in matches]
    
    tailleX, tailleY = map(int, matches[0])
    cPosDepot = tuple(map(int, matches[1])) 
    env = Environment(tailleX, tailleY, cPosDepot)
    dictAgent = {}
    generated_id = id_generator()
    
    agentConstructor = {
        "or": MyAgentGold,
        "pierres": MyAgentStones,
        "ouvr": MyAgentChest
    }
    
    for match in matches[2:]: #[2:] Removes the env size and depot coords
        match = [int(x) if i > 1 else x for i,x in enumerate(match)]
        
        if startsWith(match, 'tres'):
            env.addTreasure(Treasure(type = 1 if match[1] == 'or' else 2, value = match[-1]), *match[2:4])  
        if startsWith(match, 'AG'):
            id = next(generated_id)
            agent = agentConstructor[match[1]](id, *match[2:], env)
            dictAgent[id] = agent
            
    env.addAgentSet(dictAgent)
    return (env, dictAgent)

def main():
    env, lAg = loadFileConfig("env1.txt")
    print(env)
    for a in lAg.values() :
        print(a)

    print(vars(lAg.get("agent0")))
    #Exemple where the agents move and open a chest and pick up the treasure
    lAg.get("agent0").move(7,4,7,3)
    lAg.get("agent0").move(7, 3, 6, 3)
    lAg.get("agent0").open()
    print(env)
    lAg.get("agent0").move(6, 3, 7, 3)
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

    env.gen_new_treasures(5, 7)
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
main()