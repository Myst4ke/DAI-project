from MyAgent import MyAgent


class MyAgentChest(MyAgent) :
    def __init__(self, id, initX, initY, env):
        MyAgent.__init__(self, id, initX, initY, agentType=0, env=env)


    def open(self):
        """ Opens a chest at agent location """
        self.env.open(self, self.posX, self.posY)

    def __str__(self):
        return f"Agent chest {MyAgent.__str__(self)}"