
class Treasure:
    def __init__(self, type:int, value:int):
        """ 
        params:
            type: 1 for gold, 2 for precious stones
            value: capacity of the Treasure
        """
        self.type = type # 
        self.opened = False
        self.value = value

    def isOpen(self):
        """ return True if the chest is open, False otherwise """
        return self.open

    def openChest(self) :
        """ open the Chest """
        print("ouverture du coffre")
        self.opened = True

    def getType(self):
        """ return the type of treasure in the Chest """
        return self.type

    def getValue(self):
        """ return the quantity of treasure """
        return self.value

    def resetValue(self):
        """ set the quantity of treasure to 0 """
        self.value = 0

