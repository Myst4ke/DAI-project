from Environment import Environment
from MyAgentGold import  MyAgentGold
from MyAgentChest import MyAgentChest
from MyAgentStones import MyAgentStones
from Treasure import Treasure
import re

def startsWith(input:list, patern:str) -> bool:
    """ Return True if input list starts with patern else False """
    return True if input[0] == patern else False

def id_generator(start:int = 0):
    """ Yields ids as 'agent`n`' """
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
            print(type(agent))
            env.addAgent(agent)
            dictAgent[id] = agent
            
    env.addAgentSet(dictAgent)
    return (env, dictAgent)

def loadMoveSet(nameFile, ) -> list:
    with open(nameFile, 'r') as f:
        content = f.read()
    
    coordsPattern = r'(?::\((\d+),(\d+)\):\((\d+),(\d+)\))?'
    messagePattern = r'(?::(\w+\d))?(?::(.+))?'
    patterns = re.compile(fr'(\w+\d):(\w+){coordsPattern}{messagePattern}', re.MULTILINE)
    matches = patterns.findall(content)
    # print(matches)
    matches = [[group for group in match if group != ''] for match in matches]
    print(matches)
    for mat in matches:
        if mat[1] == "move":
            mat[2:] = map(int, mat[2:])
    return matches

# def actionMoveset(matches, env:Environment, dictAgent:dict={}):
#     moves = []
#     for match in matches:
#         agent_id, method_name, *args = match
#         if method_name == "load":
#             args=[env]
#         # print(f"{agent_id}, {method_name}, args:{args}")
#         moves.append((), args))
#         print(dictAgent.get(agent_id),method_name, args)
#     return moves 
