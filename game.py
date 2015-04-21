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
        self.tiles = [["empty" for i in range(width)] for j in range(height)]
    def show(self):
        for row in self.tiles:
            print(row)    
    def addVerticalCar(self, x, y, ID, length):
             
        self.tiles[y][x] = 'Car %d' %(ID)
        self.tiles[y+1][x] = 'Car %d' %(ID)
        if length is 3:
            self.tiles[y+2][x] = 'Car %d' %(ID)
        
    def addHorizontalCar(self, x, y, ID, length):
            
        self.tiles[y][x] = 'Car %d' %(ID)
        self.tiles[y][x+1] = 'Car %d' %(ID)
        if length is 3:
            self.tiles[y][x+2] = 'Car %d' %(ID)

    def checkIfEmpty(self, x, y):
        if y >= self.height or x >= self.width:
            return False
        if y < 0 or x < 0:
            return False
        
        if self.tiles[y][x] is 'empty':
            return True
        else:
            return False

    def checkCoordinate(self, x, y):
        print(self.tiles[y][x])


class Car(object):
    def __init__(self, orientation, board, x, y, length, carID):
        self.orientation = orientation
        # Position on board can be called by entering self.board[self.x][self.y]
        self.board = board
        self.x = x
        self.y = y
        self.length = length
        self.carID = carID
        self.free = []
        if orientation is 'horizontal':
            board.addHorizontalCar(x, y, carID, self.length)
        if orientation is 'vertical':
            board.addVerticalCar(x, y, carID, self.length)

    def isCarFree(self):
        if self.orientation is 'horizontal':
            # werkt 
            if self.x - 1 < 0 and self.x + self.length >= self.board.width:
                return False

            #Positie vrij
            if self.board.checkIfEmpty(self.x - 1,self.y) and \
            self.board.checkIfEmpty(self.x+ self.length,self.y):
                self.free = 'left, right'
                return True
            elif self.board.checkIfEmpty(self.x - 1,self.y):
                self.free = 'left'
                return True
            elif self.board.checkIfEmpty(self.x + self.length,self.y):
                self.free = 'right'
                return True
            else:
                self.free = ''
                return False
            
        if self.orientation is 'vertical':
            # Buiten bord 
            if self.y - 1 < 0 and self.y + self.length >= self.board.height:
                return False

            # Positie vrij 
            if self.board.checkIfEmpty(self.x,self.y - 1) and \
            self.board.checkIfEmpty(self.x,self.y + self.length):
                self.free = 'top, bot'
                return True
            elif self.board.checkIfEmpty(self.x,self.y - 1):
                self.free = 'top' 
                return True
            elif self.board.checkIfEmpty(self.x,self.y + self.length):
                self.free = 'bot'
                return True
            else:
                self.free = ''
                return False
    def move(self):

        if self.free == 'top, bot':
             self.free = random.choice(['top', 'bot'])
         
        if self.free == 'top':
             self.board.tiles[self.y - 1][self.x] = 'Car %d' %(self.carID)
             self.board.tiles[self.y + (self.length - 1)][self.x] = 'empty'
             self.y = self.y - 1
        elif self.free == 'bot':
             self.board.tiles[self.y + self.length][self.x] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x] = 'empty'
             self.y = self.y + 1
             
        if self.free == 'left, right':
             self.free = random.choice(['left', 'right'])
        if self.free == 'left':
             self.board.tiles[self.y][self.x - 1] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x + (self.length - 1)] = 'empty'
             self.x = self.x - 1
        elif self.free == 'right':
             self.board.tiles[self.y][self.x + self.length] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x] = 'empty'
             self.x = self.x + 1
             
    def winCoordinates(self, x, y):
        if self.board.tiles[self.y][self.x] == self.board.tiles[y][x]:
            return True
        else:
            return False

    
    
            


         

def runSimulationGame1(height, width):

    room = Board(width, height)
    # carID = 1

    # addHorizontalCar(orientation, room, x, y, length, carID)
    # red Car
    carList = []
    freeCars = []
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
  

    # Random algoritme, stopt na win of x aantal zetten
    # while redCar.winCoordinates(4, 2) == False:

    # Voorlopige loop, maakt 10 random zetten
    for i in range(50):       
        room.show()
        for currentCar in carList:
            if currentCar.isCarFree():
                freeCars.append(currentCar)     
        
        moveCar = (random.choice(freeCars))
        print ("This car is free:", moveCar.isCarFree(), ", Car ID", moveCar.carID, "It can move to position:", moveCar.free)
        

        moveCar.move()

    # TODO: auto's moeten weg worden gehaald uit de freeCars list
    # als ze niet meer free staan, of anders de list elke loop leegmaken 

    # TODO: Cars die niet meer free staan moeten uit de freeCars list
    # worden gehaald, of de move() functie moet een aparte branch hebben
    # voor Cars waarbij self.free '' is.
    # for counter in range (500):

    #     room.show()
    #     for currentCar in carList:
    #         if currentCar.isCarFree():
    #             freeCars.append(currentCar)     
        
    #     moveCar = (random.choice(freeCars))
    #     print ("This car is free:", moveCar.isCarFree(), ", Car ID", moveCar.carID, "It can move to position:", moveCar.free)
        

    #     moveCar.move()
    #     print (counter)
    # return counter

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
