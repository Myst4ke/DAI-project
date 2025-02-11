from MyAgent import MyAgent


#inherits MyAgent

class MyAgentStones(MyAgent):

    def __init__(self, id,  initX, initY, capacity, env):
        MyAgent.__init__(self, id, initX, initY, agentType=2, env=env)
        self.stone = 0
        self.backPack = capacity

    def getTreasure(self):
        """ return quantity of precious stones collected and not unloaded yet """
        return self.stone

    def unload(self):
        """ unload precious stones in the pack back at the current position """
        if self.env.unload(self):
            self.stone = 0

    def getType(self):
        """ return the agent's type """
        return 2
    
    def getCapacity(self):
        """ returns the backpack capcity of the agent """
        return self.backPack
    
    
    def load(self,env):
        """ load the treasure at the current position """
        env.load(self)

    
    def addTreasure(self, treasureValue):
        """ 
        add some precious stones to the backpack of the agent (treasureValue)
        if the quantity exceeds the back pack capacity, the remaining is lost
        """
        lastStone = self.stone
        if self.stone + treasureValue <= self.backPack:
            self.stone = self.stone + treasureValue
            return 0 # return lost value
        else :
            self.stone = self.backPack
            return lastStone + treasureValue - self.backPack # return lost value

    def __str__(self):
        return f"Agent stones {MyAgent.__str__(self)}"

