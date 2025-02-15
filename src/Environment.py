import MyAgentChest
import random
from MyAgent import MyAgent
from Treasure import Treasure

class Environment:
    def __init__(self, tailleX:int, tailleY:int, posUnload:tuple):
        self.tailleX = tailleX
        self.tailleY = tailleY
        self.grilleTres:list[list[Treasure]] = [[None for _ in range(tailleY)] for _ in range(tailleX)] # locations of Treasures
        self.grilleAgent:list[list[MyAgent]] = [[None for _ in range(tailleY)] for _ in range(tailleX)] # locations of agents
        self.posUnload = posUnload # a couple of positions x and y, where the agents can unload tresor
        self.score = 0 # quantity of treasure unload at the right place (posUnload)
        self.lostScore = 0
        self.agentSet = dict() # the set of agents acting in the environment

    def addAgent(self, agent:MyAgent):
        """ add an agent to the environment """
        posX, posY = agent.getPos()
        self.grilleAgent[posX][posY] = agent

    def addAgentSet(self, dictAgent:dict):
        """ add an agent to the set of agents """
        self.agentSet = dictAgent
        
    def addTreasure(self, tresor:Treasure, x, y):
        """ add a treasure to the environment """
        if not self.grilleTres[x][y]:
            self.grilleTres[x][y] = tresor
            for agent in self.agentSet.values():# update the agents knowledge
                agent.updateTreasureMap(tresor, x , y)

    def isAt(self, agent:MyAgent, x, y):
        """ check whether the agent is at position (x,y) """
        return self.grilleAgent[x][y] == agent

    def move(self, agent:MyAgent, x1, y1, x2, y2):
        """ make the agent moves from (x1, y1) to (x2, y2) """
        print(x1, y1, x2, y2)
        if x2 not in range(0, self.tailleX) or y2 not in range(0, self.tailleY) or x2 not in range(x1 - 1, x1 + 2) \
                or not y2 in range(y1 - 1, y1 + 2): # invalid move
            print("Env : invalid move")
            return False
        if not self.isAt(agent, x1, y1) or self.grilleAgent[x2][y2]: # position already occupied
            print("Env : position not free")
            return False
        else :
            self.grilleAgent[x2][y2] = agent
            self.grilleAgent[x1][y1] = None
            return True

    def getScore(self):
        """ return the quanity of treasure unloaded at the collector place """
        return self.score,self.lostScore

    def unload(self, agent:MyAgent):
        """ make an agent unload his bakcpack """
        if self.isAt(agent, *self.posUnload) :
            self.score = self.score + agent.getTreasure()
            print(f"Env : unloaded tres {agent.getTreasure()}")
            return True
        return False

    def open(self, agent:MyAgentChest, x, y):
        """ make a Chest Agent open the chest """
        # Agent is at given coords, chest too and chest not openend 
        if self.grilleAgent[x][y] == agent and self.grilleTres[x][y] and not self.grilleTres[x][y].opened:
            self.grilleTres[x][y].openChest()
            print("Env : chest open !")
            return True
        else:
            print("Env : no chest opened !")
            return False
    
    def load(self, agent:MyAgent):
        """ make an agent load some treasure """
        x, y = agent.getPos()
        if self.grilleAgent[x][y] != agent or (x,y) == self.posUnload or not self.grilleTres[x][y]:
            return False
        # Agent has same type as tres and tres is already opened
        if self.grilleTres[x][y].getType() == agent.getType() and self.grilleTres[x][y].opened:
            self.lostScore += agent.addTreasure(self.grilleTres[x][y].getValue())
            self.grilleTres[x][y] = None
            print("Env : load OK")
            return True
        else :
            print("Env : load fail")
            return False

    def send(self,idSender, idReceiver, textContent):
        """ make an agent send a message """
        self.agentSet[idReceiver].receive(idSender, textContent)

    def gen_new_treasures(self, nb:int, maxVal:int):
        """ generates X new treasures at random coords """
        for _ in range(nb) :
            x = random.randint(0,self.tailleX - 1)
            y = random.randint(0,self.tailleY - 1)
            treasureType = random.randint(1,2)
            treasureValue = random.randint(1, maxVal)
            print("Env : new tres at", x, y)
            self.addTreasure(Treasure(treasureType, treasureValue), x, y)

    def __str__(self):
        str = "    0   1   2   3   4   5   6   7   8   9  10  11\n0 "
        for i in range(self.tailleX) :
            str+='|'
            for j in range(self.tailleY) :
                if self.grilleTres[i][j]:
                    if self.grilleTres[i][j].getType() == 1:
                        str += " G "
                    else :
                        str += " S "
                elif self.grilleAgent[i][j]:
                    str += " A "
                else:
                    str += " - "
                str += "|"
            str += f"\n{i+1} " if (i+1)//10 < 1 else f"\n{i+1}"
        return str