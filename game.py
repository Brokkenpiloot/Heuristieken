# Heuristieken.
# Joost Jason en Joren.
# RushHour.
#
import random

class Board(object):
    def __init__(self, width, height):
        # Generate empty board as list of lists
        self.height = height
        self.width = width
        self.board = [["empty" for i in range(width)] for j in range(height)]
    def show(self):
        for row in self.board:
            print(row)    
    def addVerticalCar(self, x, y, ID, length):
        # TODO: create car object 
        
        self.board[y][x] = 'Car %d' %(ID)
        self.board[y+1][x] = 'Car %d' %(ID)
        if length is 3:
            self.board[y+2][x] = 'Car %d' %(ID)
        
    def addHorizontalCar(self, x, y, ID, length):
        # TODO: create car object 
        
        self.board[y][x] = 'Car %d' %(ID)
        self.board[y][x+1] = 'Car %d' %(ID)
        if length is 3:
            self.board[y][x+2] = 'Car %d' %(ID)

    def checkIfEmpty(self, x, y):
        if self.board[y][x] is 'empty':
            return True
        else:
            return False

    def checkCoordinate(self, x, y):
        print(self.board[y][x])

class Car(object):
    def __init__(self, orientation, board, x, y, length, carID):
        self.orientation = orientation
        # Position on board can be called by entering self.board[self.x][self.y]
        self.board = board
        self.x = x
        self.y = y
        self.length = length
        self.carID = carID
        if orientation is 'horizontal':
            board.addHorizontalCar(x, y, carID, self.length)
        if orientation is 'vertical':
            board.addVerticalCar(x, y, carID, self.length)

    def isCarFree(self):
        # Functie heeft nog wat fouten
        if self.orientation is 'horizontal':
            # dit if-statement moet in ieder geval 'and' worden
            if self.x - 1 < 0 or self.x + self.length >= self.board.width:
                return False
            # onderstaand if-statement geeft soms een 'list index out of range'
            # als het bovenstaande if-statement 'and' gebruikt.
            # we moeten even onderzoeken hoe dat samenhangt. 
            if self.board.checkIfEmpty(self.x - 1,self.y) or \
            self.board.checkIfEmpty(self.x + self.length,self.y):
                return True
            else:
                return False

            
        if self.orientation is 'vertical':
            if self.y - 1 < 0 or self.y + self.length >= self.board.height:
                return False
            if self.board.checkIfEmpty(self.x,self.y - 1) or \
            self.board.checkIfEmpty(self.x,self.y + self.length):
                return True
            else:
                return False

def runSimulationGame1(height, width):

    room = Board(width, height)
    # carID = 1

    # addHorizontalCar(orientation, room, x, y, length, carID)
    # red Car
    carList = []
    redCar = Car('horizontal', room, 3, 2, 2, 1)

    # Traffic
    traffic1 = Car('vertical', room, 2, 0, 3, 2)
    traffic2 = Car('horizontal', room, 3, 0, 2, 3)
    traffic3 = Car('vertical', room, 5, 0, 3, 4)
    traffic4 = Car('vertical', room, 3, 3, 3, 5)
    traffic5 = Car('horizontal', room, 4, 3, 2, 6)
    traffic6 = Car('vertical', room, 0, 4, 2, 7)
    traffic7 = Car('horizontal', room, 1, 4, 2, 8)
    traffic8 = Car('horizontal', room, 4, 5, 2, 9)
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, traffic8]
    
    room.show()
    # Zoekt random Car en kijkt of ie free staat
    # (kan misschien ook ergens anders als aparte method?)
    currentCar = (random.choice(carList))
    print ("This car is free:", currentCar.isCarFree(), ", Car ID", currentCar.carID)

    #TODO: move etc.

    # Tijdelijk weggecomment zodat simulatie 1 gerund kan worden
    """   
def runSimulationGame2(height, width):
    room = board(width, height)

    # red car
    addHorizontalCar(3, 2, 1, 2)

    # Traffic
    addHorizontalCar(2, 0, 2, 2)
    addHorizontalCar(4, 0, 3, 2)
    addHorizontalCar(1, 1, 4, 2)
    addHorizontalCar(3, 1, 5, 2)
    addVerticalCar(5, 1, 6, 3)
    addVerticalCar(4, 2, 7, 2)
    addHorizontalCar(0, 3, 8, 2)
    addHorizontalCar(2, 3, 9, 2)
    addVerticalCar(0, 4, 10, 2)
    addVerticalCar(3, 4, 11, 2)
    addHorizontalCar(4, 4, 12, 2)
    addHorizontalCar(4, 5, 12, 2)

    room.show()

def runSimulationGame2(height, width):
    room = board(width, height)

    # red car
    addHorizontalCar(0, 2, 1, 2)

    # Traffic
    addHorizontalCar(1, 0, 2, 2)
    addHorizontalCar(3, 0, 3, 3)
    addHorizontalCar(1, 1, 4, 2)
    addVerticalCar(3, 1, 5, 2)
    addHorizontalCar(4, 1, 6, 2)
    addVerticalCar(2, 2, 7, 2)
    addVerticalCar(5, 2, 8, 2)
    addHorizontalCar(0, 3, 9, 2)
    addHorizontalCar(3, 3, 10, 2)
    addVerticalCar(0, 4, 11, 2)
    addVerticalCar(2, 4, 12, 2)
    addHorizontalCar(4, 4, 13, 2)

"""
    room.show()

