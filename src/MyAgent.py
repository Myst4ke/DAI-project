class MyAgent:
    def __init__(self, id, initX, initY, env):
        self.id = id
        self.posX = initX
        self.posY = initY
        self.env = env
        self.mailBox = []

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
        print(f"mail received from {idSender} with content {textContent}")
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

    def __str__(self):
        return f"{self.id} ({self.posX} , {self.posY})"

