# Heuristieken.
# Joost Jason en Joren.
# RushHour.
# 

import random
class Board(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.tiles = [["empty" for i in range(width)] for j in range(height)]
        self.storage = set()
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
        
    def convertState(self):
        # List of lists to String conversion
        state = ''
        for i in range(self.height):
            state = state + ''.join(self.tiles[i])
        return state
    
    def saveState(self, state):
        # Voegt state string toe aan set
        self.storage.add(state)
        
    def compareState(self, state):
        # Zoekt of state string bestaat in set, return true indien ja
        return state in self.storage
    
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
        self.moved = False
        self.lastMove = ''
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
                self.free = ['left', 'right']
                return True
            elif self.board.checkIfEmpty(self.x - 1,self.y):
                self.free = ['left']
                return True
            elif self.board.checkIfEmpty(self.x + self.length,self.y):
                self.free = ['right']
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
                self.free = ['top', 'bot']
                return True
            elif self.board.checkIfEmpty(self.x,self.y - 1):
                self.free = ['top'] 
                return True
            elif self.board.checkIfEmpty(self.x,self.y + self.length):
                self.free = ['bot']
                return True
            else:
                self.free = ''
                return False

            ## Hier heb ik 'direction' aan toegevoegd, om niet meer afhankelijk te hoeven zijn
            ## van self.free
    def move(self, direction):

        if direction == 'top':
             self.board.tiles[self.y - 1][self.x] = 'Car %d' %(self.carID)
             self.board.tiles[self.y + (self.length - 1)][self.x] = 'empty'
             self.y = self.y - 1
        elif direction == 'bot':
             self.board.tiles[self.y + self.length][self.x] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x] = 'empty'
             self.y = self.y + 1
             
        if direction == 'left':
             self.board.tiles[self.y][self.x - 1] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x + (self.length - 1)] = 'empty'
             self.x = self.x - 1
        elif direction == 'right':
             self.board.tiles[self.y][self.x + self.length] = 'Car %d' %(self.carID)
             self.board.tiles[self.y][self.x] = 'empty'
             self.x = self.x + 1

    def winCoordinates(self, x, y):
        if self.board.tiles[self.y][self.x] == self.board.tiles[y][x]:
            return True
        else:
            return False

def reverseLastMove(carToReverse):
        tussen = []
        moveToReverse = carToReverse.lastMove
        if moveToReverse == ['left']:
            tussen = ['right']
        elif moveToReverse == ['right']:
            tussen = ['left']
        elif moveToReverse == ['top']:
            tussen = ['bot']
        elif moveToReverse == ['bot']:
            tussen = ['top']
        carToReverse.move("%s" %tussen)
        print ('Car reversed')
        print ("reverse show")

def runSimulationGame1():

    room = Board(6, 6)
    # carID = 1

    # addHorizontalCar(orientation, room, x, y, length, carID)
    # red Car
    carList = []
    freeCars = []
    moveList = []
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

    # Algoritme, stopt na win of x aantal zetten
    ## Drie nieuwe variabelen toegevoegd die helpen het niveau bij te houden.
    counter = 0
    level = 0
    movesPerLevel = {}
    direction = ''
    # while redCar.winCoordinates(5, 2) == False:
    for i in range (0, 4):
        room.show()
                       
        # Opslaan van huidige boardstate als hij nog niet in
        # de storage staat
        ## Reverse move maakt ook level eentje kleiner, en cleart de movesPerLevel
        ## van het niveau dat achter gelaten wordt.
        state = room.convertState()
        movesPerLevel[level] = movesPerLevel.get(level, [])
        if room.compareState(state) == False:
            room.saveState(state)
            for i in freeCars: 
                i.moved = False
            print ('New state found')
        else:
            print ('No new state found: ')
            if len(movesPerLevel[level - 1]) == 0:
                reverseLastMove(moveList[-1][0])
                moveList.pop(-1)
                #room.show()
                moveCar.moved = True
                movesPerLevel[level] = []
                level = level - 2
            else: 
                reverseLastMove(moveList[-1][0])
                moveCar.moved = True
                movesPerLevel[level] = []
                level = level - 1       	
            room.show()
            print
            print
            print

            # Kiest random car uit alle cars die vrijstaan en beweegt hem
            ## Als je op een niveau komt waar al een keer alle moves voor zijn gevonden,
            ## hoef je het niet nog een keer te checken. 
            
        if len(movesPerLevel[level]) == 0:
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree():
                    freeCars.append(currentCar)
                    for direction in currentCar.free:
                        movesPerLevel[level].append(currentCar)
                        movesPerLevel[level].append(direction)

                        
        # iterate door alle car objects in movesPerLevel en update self.free waarden automatisch
        for i in movesPerLevel[level][::2]:
            if i.isCarFree() == False:
                movesPerLevel[level].pop(i)
                movesPerLevel[level].pop(i)
                        

        print (movesPerLevel[level])
        #print ('Moves to be made this round:', movesPerLevel[level])
            
        ## Hier moet ie dus de eerste auto uit movesPerLevel pakken.
        ## Wat ik probeer te fixxen is dat dat dan de eerste waarde in de list zou zijn.
        ## Dictionaries zijn alleen het foute data type... Weet even niet welke ik wel
        ## moet hebben.
        ## Daarbij moet moveList nu, doordat we niet meer alleen op self.free af gaan,
        ## de auto, maar ook de direction op slaan.
        moveCar = (movesPerLevel[level][0])
        print (moveCar)   
        print ("This car is free:", moveCar.isCarFree(), ", Car ID", moveCar.carID, \
                   "It can move to position(s):", moveCar.free)
        moveList.append((moveCar, movesPerLevel[level][1]))

        ## Hier zou dan de tweede waarde de move zijn die hij moet uitvoeren.
        # print movesPerLevel[level][1]
        moveCar.move("%s" %movesPerLevel[level][1])
        # print
        # print
        # print
        # print ("Move Happened")
        # room.show()


        moveCar.lastMove = movesPerLevel[level][1]
            
        ## Hier zou hij dan de zet die net gedaan is deleten uit de lijst. 
        movesPerLevel[level].pop(0)
        movesPerLevel[level].pop(0)    

        # Update counters en print info
        level = level + 1
        counter = counter + 1
        print ("Counter: %i" %counter)
        print ("Level: %i" %level)
            
        # maakt freeCars list weer leeg
        freeCars[:] = []

        # print ("move show")
        # print 
        # print 
        # room.show()
        # print 
        # print
            # counter om loop eerder te breken
            #if counter is 20:
                #break
            
    # toont het aantal unieke states/zetten die zijn gemaakt en
    # de moves die zijn gemaakt
    print ("States stored:")
    print (len(room.storage))
    room.show()
    return counter


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
