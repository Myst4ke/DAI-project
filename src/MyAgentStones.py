from MyAgent import MyAgent


#inherits MyAgent

class MyAgentStones(MyAgent):

    def __init__(self, id,  initX, initY, capacity, env):
        MyAgent.__init__(self, id, initX, initY, env)
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
        if self.gold + treasureValue <= self.backPack:
            self.gold = self.gold + treasureValue
        else :
            self.gold = self.backPack

    def __str__(self):
        return f"Agent stones {MyAgent.__str__(self)}"

