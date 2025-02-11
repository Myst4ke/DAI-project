import math
import copy
    
def distance(p1:tuple, p2:tuple):
        return math.dist(p1, p2)
    
class MyAgent:
    def __init__(self, id, initX, initY, agentType, env):
        self.id = id
        self.posX = initX
        self.posY = initY
        self.env = env
        self._treasureMap = copy.deepcopy(env.grilleTres)
        self.mailBox = []
        self.type = agentType
        self.closestChest:list[tuple] = []
        self.reservedChest = None
        self.stone = None
        self.gold = None
        self.backPack = None
        self.nbMove = 0
        
    def open(self):
        """ Opens a chest at agent location """
        if self.env.open(self, self.posX, self.posY):
            self._treasureMap[self.posX][self.posY] = None
    def load(self,env):
        """ load the treasure at the current position """
        if env.load(self):
            self._treasureMap[self.posX][self.posY] = None
    def unload(self):...
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.getId() == self.getId()
        return False


    def move(self,  x1,y1, x2,y2) :
        """ make the agent moves from (x1,y1) to (x2,y2) """
        if x1 == self.posX and y1 == self.posY :
            print("departure position OK")
            if self.env.move(self, x1, y1, x2, y2) :
                self.posX = x2
                self.posY = y2
                self.nbMove += 1
                print("deplacement OK")
                return 1

        return -1

    def getId(self):
        """ return the id of the agent """
        return self.id


    def getPos(self):
        """ return the position of the agent """
        return (self.posX, self.posY)


    def receive(self, idReceiver, textContent):
        """ add a message to the agent's mailbox """
        self.mailBox.append((idReceiver, textContent))


    def readMail(self):
        """ 
        the agent reads a message in her mailbox (FIFO mailbox)
        return a tuple (id of the sender, message  text content)
        """
        idSender, textContent = self.mailBox.pop(0)
        print(f"{self.id} : mail received from {idSender} with content '{textContent}'")
        return (idSender, textContent)


    def send(self, idReceiver, textContent):
        """ send a message to the agent whose id is idReceiver """
        self.env.send(self.id, idReceiver, textContent)

    def getCapacity(self):
        """ Returns the amount of gold/stones that can be stored by agent """
        return 0
    
    def getTreasure(self):
        """ Returns the amount of gold/stones stored by agent """
        return 0
    
    def updateTreasureMap(self, tresor, x , y):
        """ Update private knowledge when chest added """
        self._treasureMap[x][y] = tresor
    
    def _getClosestChest(self):
        """ Update self.closestChest with nearest tresures, sorted by distance"""
        grilleTres = self._treasureMap
        self.closestChest = []
        for x in range(len(grilleTres)):
            for y in range(len(grilleTres[x])):
                if grilleTres[x][y]:
                    # print(f"{self.id}: {x,y} = {grilleTres[x][y]}, selftype: {self.type}, type: {grilleTres[x][y].getType()}, opened: {grilleTres[x][y].opened}")
                    if grilleTres[x][y].getType() == self.type and self.env.grilleTres[x][y].opened: # agent gold or stone and opened
                        self.closestChest.append((distance((x,y), (self.posX, self.posY)), (x,y)))
                    elif self.type == 0 and not grilleTres[x][y].opened:  # agent chest
                        self.closestChest.append((distance((x,y), (self.posX, self.posY)), (x,y)))
        self.closestChest.sort(key=lambda x: x[0])
        print(f'{self.id}({self.posX,self.posY}) : closest chests =  {self.closestChest}')
        
    def _reserveClosest(self):
        """ Update the reserved chest """
        self.reservedChest = self.closestChest[0][1] if len(self.closestChest) > 0 else None
        print(f'{self.id} : reserved chest {self.reservedChest}')
    
    def _sendReserve(self):
        """ send other agent to remove chest from their knowledge """
        print(f'{self.id} : sending reserved chest')
        for ag in self.env.agentSet.values():
            # send reserve chest only to same agent type and only if not None
            if ag.type == self.type and self.reservedChest: 
                self.send(ag.id, f"{self.reservedChest}")     
                  
    def _deleteReservedChests(self):
        for _ in range(len(self.mailBox)):
            _, text = self.readMail()
            x,y = text[1:-1].split(",") #removes parentheses and comma to get coordinates
            print(f'{self.id} : deleting chest {x,y}')
            self._treasureMap[int(x)][int(y)] = None
            
    def _nearestCell(self, goalX, goalY):        
        """ returns the coords of the nearest cell closest to goal """
        # Déplacement direct vers la meilleure case
        new_x = self.posX + (1 if goalX > self.posX else -1 if goalX < self.posX else 0)
        new_y = self.posY + (1 if goalY > self.posY else -1 if goalY < self.posY else 0)

        # Vérifier si la case est libre
        if not self.env.grilleAgent[new_x][new_y]:
            return new_x, new_y

        # Liste des cases adjacentes possibles triées par proximité avec le but
        mouvements = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # Trier les cases par distance croissante au but
        cases_triees = sorted(
            [(self.posX + dx, self.posY + dy) for dx, dy in mouvements],
            key=lambda case: abs(case[0] - goalX) + abs(case[1] - goalY)  # Distance de Manhattan
        )

        # Trouver la première case vide
        for x, y in cases_triees:
            if not self.env.grilleAgent[x][y]:
                return x, y

        # Si aucune case libre, rester sur place
        return self.posX, self.posY
    
    def next_move(self):
        self._deleteReservedChests()
        self._getClosestChest()
        if not self.reservedChest:
            if (self.gold or self.stone) and (self.gold == self.backPack or self.stone == self.backPack):
                self.reservedChest = self.env.posUnload
            else:
                self._reserveClosest()
                self._sendReserve()
        else:
            if (self.posX,self.posY) == self.reservedChest:
                print(f"{self.id} at {self.posX,self.posY} wants to open/load chest at {self.reservedChest}")
                if self.type == 0 : #agent chest
                    self.open()
                else: #agent stone/gold
                    self.load(self.env)
                    self.unload()
                self.reservedChest = None
            else:
                self.move(self.posX, self.posY, *self._nearestCell(*self.reservedChest))

    def __str__(self):
        return f"{self.id} ({self.posX} , {self.posY})"

