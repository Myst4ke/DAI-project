from MyAgent import MyAgent


#inherits MyAgent

class MyAgentStones(MyAgent):

    def __init__(self, id,  initX, initY, capacity, env):
        MyAgent.__init__(self, id, initX, initY, env)
        self.stone = 0
        self.backPack = capacity

    # return quantity of precious stones collected and not unloaded yet
    def getTreasure(self):
        return self.stone

    # unload precious stones in the pack back at the current position
    def unload(self):
        self.env.unload(self)
        self.stone = 0

    #return the agent's type
    def getType(self):
        return 2
    
    def getCapacity(self):
        return self.backPack
    # load the treasure at the current position
    def load(self,env):
        env.load(self)

    # add some precious stones to the backpack of the agent (quantity t)
    # if the quantity exceeds the back pack capacity, the remaining is lost
    def addTreasure(self, t):
        if(self.stone + t <= self.backPack) :
            self.stone = self.stone + t
        else :
            self.stone = self.backPack

    def __str__(self):
        return f"Agent stones {MyAgent.__str__(self)}"

