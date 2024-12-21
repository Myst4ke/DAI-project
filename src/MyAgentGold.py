from MyAgent import MyAgent


#inherits MyAgent

class MyAgentGold(MyAgent):

    def __init__(self, id, initX, initY, capacity, env):
        MyAgent.__init__(self, id, initX, initY, env)
        self.gold = 0 # the quantity of gold collected and not unloaded yet
        self.backPack = capacity #capacity of the agent's back pack


    def getTreasure(self):
        """ return quantity of gold collected and not unloaded yet """
        return self.gold

    def unload(self):
        """ unload gold in the pack back at the current position """
        if self.env.unload(self):
            self.gold = 0

    def getType(self):
        """ return the agent's type """
        return 1

    def getCapacity(self):
        """ returns the backpack capcity of the agent """
        return self.backPack
    
    
    def addTreasure (self, treasureValue:int):
        """ 
        Add some gold to the backpack of the agent (treasureValue)
        if the quantity exceeds the back pack capacity, the remaining is lost 
        """
        if self.gold + treasureValue <= self.backPack:
            self.gold = self.gold + treasureValue
        else :
            self.gold = self.backPack

    def load(self,env):
        """ load the treasure at the current position """
        env.load(self)

    def __str__(self):
        return f"Agent gold {MyAgent.__str__(self)}"