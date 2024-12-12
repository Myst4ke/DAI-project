
import MyAgent, MyAgentChest
import random
from Treasure import Treasure

class Environment:

    def __init__(self, tailleX:int, tailleY:int, posUnload:tuple):
        self.tailleX = tailleX
        self.tailleY = tailleY
        self.grilleTres = [[None for _ in range(tailleY)] for _ in range(tailleX)] # locations of Treasures
        self.grilleAgent = [[None for _ in range(tailleY)] for _ in range(tailleX)] # locations of agents
        self.posUnload = posUnload # a couple of positions x and y, where the agents can unload tresor
        self.score = 0 # quantity of treasure unload at the right place (posUnload)
        self.agentSet = dict() # the set of agents acting in the environment


    # add an agent to the environment
    def addAgent(self, agent:MyAgent):
        posX, posY = agent.getPos()
        self.grilleAgent[posX][posY] = agent

    #add a treasure to the environment
    def addTreasure(self, tresor : Treasure, x, y):
        if(self.grilleTres[x][y] == None):
            self.grilleTres[x][y] =  tresor

    # add an agent to the set of agents
    def addAgentSet(self, dictAgent):
        self.agentSet = dictAgent

    # check whether the agent is at position (x,y)
    def isAt(self, agent:MyAgent, x, y):
        return self.grilleAgent[x][y] == agent

    # make the agent moves from (x1, y1) to (x2, y2)
    def move(self, agent:MyAgent, x1, y1, x2, y2):
        if x2 < 0 or y2 < 0 or x2 >= self.tailleX or y2 >= self.tailleY or ( x2 != x1 -1 and  x2 != x1+1 and x2 != x1) \
                or ( y2!= y1 -1 and  y2 != y1+1 and y2!=y1) : # invalid move
            print("invalid move")
            return False
        if ( not self.isAt(agent, x1, y1)) or self.grilleAgent[x2][y2] != None  : # position already occupied
            print("position not free")
            return False
        else :
            self.grilleAgent[x2][y2] = agent
            self.grilleAgent[x1][y1] = None
            return True

    # return the quanity of treasure unloaded at the collector place
    def getScore(self):
        return self.score

    # make an agent unload her bakcpack
    def unload(self, agent:MyAgent):
        if self.isAt(agent, self.posUnload[0], self.posUnload[1]) :
            self.score = self.score + agent.getTreasure()
            print("unload tres : {}".format(agent.getTreasure()))

    # make a Chest Agent open the chest
    def open(self, agent:MyAgentChest, x, y):
        if(self.grilleAgent[x][y] == agent and self.grilleTres[x][y] != None) :
            self.grilleTres[x][y].openChest()
            print("chest open !")

    # make an agent load some treasure
    def load(self, agent ):
        x , y = agent.getPos()
        if(self.grilleTres[x][y] != None  and self.grilleTres[x][y].getType() == agent.getType() ) :
            print("load OK")
            agent.addTreasure(self.grilleTres[x][y].getValue())
            self.grilleTres[x][y].resetValue()
        else :
            print("load fail")

    #make an agent send a message
    def send(self,idSender, idReceiver, textContent):
        self.agentSet[idReceiver].receive(idSender, textContent)

    def gen_new_treasures(self, nb, maxVal):
        for i in range(nb) :
            x = random.randint(0,self.tailleX - 1)
            y = random.randint(0,self.tailleY - 1)
            t = random.randint(0,1)
            v = random.randint(1, maxVal)
            print("new tres at", x, y)
            self.addTreasure(Treasure(t,v), x, y)


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