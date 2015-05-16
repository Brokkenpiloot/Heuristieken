# Heuristieken.
# Joost Jason en Joren.
# RushHour.
# 

import random
import copy
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

        # self.free = []
        # self.moved = False
        # self.lastMove = '' 
        if orientation is 'horizontal':
            board.addHorizontalCar(x, y, carID, self.length)
        if orientation is 'vertical':
            board.addVerticalCar(x, y, carID, self.length)

    def isCarFree(self):
        if self.orientation is 'horizontal':
            # werkt 
            if self.x - 1 < 0 and self.x + self.length >= self.board.width:
                return ['']

            #Positie vrij
            if self.board.checkIfEmpty(self.x - 1,self.y) and \
            self.board.checkIfEmpty(self.x+ self.length,self.y):
                return ['left', 'right']

            elif self.board.checkIfEmpty(self.x - 1,self.y):
                return  ['left']

            elif self.board.checkIfEmpty(self.x + self.length,self.y):
                return ['right']
            else:
                return ['']

            
        if self.orientation is 'vertical':
            # Buiten bord 
            if self.y - 1 < 0 and self.y + self.length >= self.board.height:
                return ['']

            # Positie vrij 
            if self.board.checkIfEmpty(self.x,self.y - 1) and \
            self.board.checkIfEmpty(self.x,self.y + self.length):
                return ['top', 'bot']

            elif self.board.checkIfEmpty(self.x,self.y - 1):
                return ['top'] 

            elif self.board.checkIfEmpty(self.x,self.y + self.length):
                return ['bot']

            else:
                return ['']

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

    def altWinCoordinates(self):
        tilesToCheck = self.board.width - (self.x + 2)
        for i in range(0, tilesToCheck):
            if self.board.tiles[self.y][self.x + 2] != 'empty':
                return False
        return True

# Eerste skelet van een game class
class game(object):
    def __init__(self, board):
        self.board = board
        self.carList = []

    #def runAlgorithme():
        

def reverseLastMove(carToReverse, direction):
        tussen = ''
        if direction == 'left':
            tussen = 'right'
        elif direction == 'right':
            tussen = 'left'
        elif direction == 'top':
            tussen = 'bot'
        elif direction == 'bot':
            tussen = 'top'
        carToReverse.move("%s" %tussen)

def possibleMoves(): 
    if len(movesPerLevel[level]) == 0:
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    for direction in currentCar.isCarFree():
                        movesPerLevel[level].append((currentCar, direction))

def runSimulationGame1():
    totaal = 0
    room = Board(6, 6)
    # carID = 1

    # addHorizontalCar(orientation, room, x, y, length, carID)
    # red Car
    carList = []
    freeCars = []
    level = 0
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
    movesPerLevel = {}
    direction = ''
    counter = 0
    reverseSwitched = False
    winConHor = 5
    winConVer = 2
    
    while redCar.winCoordinates(winConHor, winConVer) == False:
    # for i in range(0,1):
        reverseSwitched = False
        room.show()
        movesPerLevel[level] = movesPerLevel.get(level, [])
        state = room.convertState()
        # movesPerLevel[level] = movesPerLevel.get(level, [])
        # movesPerLevel2[level] = movesPerLevel2.get(level, [])
        # checker = 0
        # checker2 = 0

        if room.compareState(state) == False:
            room.saveState(state)
            for i in freeCars: 
                i.moved = False
            print ('New state found')
            reverseSwitched = False
        else:
            reverseSwitched = True
            print ('No new state found: ')
            if len(movesPerLevel[level - 1]) == 0:
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                # movesPerLevel[level] = []
                level = level - 2
            else: 
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                level = level - 1       
            room.show()
        
        if len(movesPerLevel[level]) == 0:
            movesPerLevel[level] = []
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    checker3 = 0
                    for i in range(0, len(currentCar.isCarFree())):
                        direction = currentCar.isCarFree()[checker3]
                        movesPerLevel[level].append((currentCar, direction))
                        checker3 += 1

        totaal += len(movesPerLevel[level])

        print (len(movesPerLevel[level]))
        print ("totaal")
        print (totaal)

        # ########## Random version
        randomCar = random.choice(movesPerLevel[level])
        print (randomCar)
        moveCar = randomCar[0]
        print (moveCar)
        print ("Car ID", moveCar.carID, \
                   "It can move to position(s):", moveCar.isCarFree())
        print (randomCar[1])
        moveList.append(randomCar)
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].remove(randomCar)


        # ####### normal version
        # moveCar = (movesPerLevel[level][0][0])
        # print ("Car ID", moveCar.carID, \
        #            "It can move to position(s):", moveCar.isCarFree())
        # print (movesPerLevel[level][0][1])
        # moveList.append(movesPerLevel[level][0])
        # moveCar.move("%s" %moveList[-1][1])
        # movesPerLevel[level].pop(0)    





        level = level + 1
        counter = counter + 1
        print ("Counter: %i" %counter)
        print ("Level: %i" %level)
            
        # maakt freeCars list weer leeg
        freeCars[:] = []

    # toont het aantal unieke states/zetten die zijn gemaakt en
    # de moves die zijn gemaakt
    print ("States stored:")
    print (len(room.storage))
    room.show()
    print (len(moveList))

      
def runSimulationGame2():
    totaal = 0
    room = Board(6, 6)
    carList = []
    freeCars = []
    level = 0
    moveList = []
    
    # red car
    redCar = Car('horizontal', room, 2, 2, 2, 1)
    # Traffic
    traffic1 = Car('horizontal', room, 2, 0, 2, 2)
    traffic2 = Car('horizontal', room, 4, 0, 2, 3)
    traffic3 = Car('horizontal', room, 1, 1, 2, 5)
    traffic4 = Car('horizontal', room, 3, 1, 2, 6)
    traffic5 = Car('vertical', room, 5, 1, 3, 7)
    traffic6 = Car('vertical', room, 4, 2, 2, 8)
    traffic7 = Car('horizontal', room, 0, 3, 2, 9)
    traffic8 = Car('horizontal', room, 2, 3, 2, 10)
    traffic9 = Car('vertical', room, 0, 4, 2, 11)
    traffic10 = Car('vertical', room, 3, 4, 2, 12)
    traffic11 = Car('horizontal', room, 4, 4, 2, 13)
    traffic12 = Car('horizontal', room, 4, 5, 2, 14)
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12] 
    movesPerLevel = {}
    direction = ''
    counter = 0
    reverseSwitched = False
    winConHor = 5
    winConVer = 2

    while redCar.winCoordinates(winConHor, winConVer) == False:
    # for i in range(0,1):
        reverseSwitched = False
        room.show()
        movesPerLevel[level] = movesPerLevel.get(level, [])
        state = room.convertState()
        # movesPerLevel[level] = movesPerLevel.get(level, [])
        # movesPerLevel2[level] = movesPerLevel2.get(level, [])
        # checker = 0
        # checker2 = 0

        if room.compareState(state) == False:
            room.saveState(state)
            for i in freeCars: 
                i.moved = False
            print ('New state found')
            reverseSwitched = False
        else:
            reverseSwitched = True
            print ('No new state found: ')
            if len(movesPerLevel[level - 1]) == 0:
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                # movesPerLevel[level] = []
                level = level - 2
            else: 
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                level = level - 1       
            room.show()
        
        if len(movesPerLevel[level]) == 0:
            movesPerLevel[level] = []
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    checker3 = 0
                    for i in range(0, len(currentCar.isCarFree())):
                        direction = currentCar.isCarFree()[checker3]
                        movesPerLevel[level].append((currentCar, direction))
                        checker3 += 1

        totaal += len(movesPerLevel[level])

        print (len(movesPerLevel[level]))
        print ("totaal")
        print (totaal)

        # ########## Random version
        randomCar = random.choice(movesPerLevel[level])
        print (randomCar)
        moveCar = randomCar[0]
        print (moveCar)
        print ("Car ID", moveCar.carID, \
                   "It can move to position(s):", moveCar.isCarFree())
        print (randomCar[1])
        moveList.append(randomCar)
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].remove(randomCar)


        # ####### normal version
        # moveCar = (movesPerLevel[level][0][0])
        # print ("Car ID", moveCar.carID, \
        #            "It can move to position(s):", moveCar.isCarFree())
        # print (movesPerLevel[level][0][1])
        # moveList.append(movesPerLevel[level][0])
        # moveCar.move("%s" %moveList[-1][1])
        # movesPerLevel[level].pop(0)    





        level = level + 1
        counter = counter + 1
        print ("Counter: %i" %counter)
        print ("Level: %i" %level)
            
        # maakt freeCars list weer leeg
        freeCars[:] = []

    # toont het aantal unieke states/zetten die zijn gemaakt en
    # de moves die zijn gemaakt
    print ("States stored:")
    print (len(room.storage))
    room.show()
    print (len(moveList))


def runSimulationGame3():
    totaal = 0
    room = Board(6, 6)
    carList = []
    freeCars = []
    level = 0
    moveList = []
    
    # red car
    redCar = Car('horizontal', room, 0, 2, 2, 1)
    # Traffic
    traffic1 = Car('horizontal', room, 1, 0, 2, 2)
    traffic2 = Car('horizontal', room, 3, 0, 3, 3)
    traffic3 = Car('horizontal', room, 1, 1, 2, 5)
    traffic4 = Car('vertical', room, 3, 1, 2, 6)
    traffic5 = Car('horizontal', room, 4, 1, 2, 7)
    traffic6 = Car('vertical', room, 2, 2, 2, 8)
    traffic7 = Car('vertical', room, 5, 2, 2, 9)
    traffic8 = Car('horizontal', room, 0, 3, 2, 10)
    traffic9 = Car('horizontal', room, 3, 3, 2, 11)
    traffic10 = Car('vertical', room, 0, 4, 2, 12)
    traffic11 = Car('vertical', room, 2, 4, 2, 13)
    traffic12 = Car('horizontal', room, 4, 4, 2, 14)
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12] 
    movesPerLevel = {}
    direction = ''
    counter = 0
    reverseSwitched = False
    winConHor = 5
    winConVer = 2

    while redCar.winCoordinates(winConHor, winConVer) == False:
    # for i in range(0,1):
        reverseSwitched = False
        room.show()
        movesPerLevel[level] = movesPerLevel.get(level, [])
        state = room.convertState()
        # movesPerLevel[level] = movesPerLevel.get(level, [])
        # movesPerLevel2[level] = movesPerLevel2.get(level, [])
        # checker = 0
        # checker2 = 0

        if room.compareState(state) == False:
            room.saveState(state)
            for i in freeCars: 
                i.moved = False
            print ('New state found')
            reverseSwitched = False
        else:
            reverseSwitched = True
            print ('No new state found: ')
            if len(movesPerLevel[level - 1]) == 0:
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                # movesPerLevel[level] = []
                level = level - 2
            else: 
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                level = level - 1       
            room.show()
        
        if len(movesPerLevel[level]) == 0:
            movesPerLevel[level] = []
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    checker3 = 0
                    for i in range(0, len(currentCar.isCarFree())):
                        direction = currentCar.isCarFree()[checker3]
                        movesPerLevel[level].append((currentCar, direction))
                        checker3 += 1

        totaal += len(movesPerLevel[level])

        print (len(movesPerLevel[level]))
        print ("totaal")
        print (totaal)

        # ########## Random version
        randomCar = random.choice(movesPerLevel[level])
        print (randomCar)
        moveCar = randomCar[0]
        print (moveCar)
        print ("Car ID", moveCar.carID, \
                   "It can move to position(s):", moveCar.isCarFree())
        print (randomCar[1])
        moveList.append(randomCar)
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].remove(randomCar)


        # ####### normal version
        # moveCar = (movesPerLevel[level][0][0])
        # print ("Car ID", moveCar.carID, \
        #            "It can move to position(s):", moveCar.isCarFree())
        # print (movesPerLevel[level][0][1])
        # moveList.append(movesPerLevel[level][0])
        # moveCar.move("%s" %moveList[-1][1])
        # movesPerLevel[level].pop(0)    





        level = level + 1
        counter = counter + 1
        print ("Counter: %i" %counter)
        print ("Level: %i" %level)
            
        # maakt freeCars list weer leeg
        freeCars[:] = []

    # toont het aantal unieke states/zetten die zijn gemaakt en
    # de moves die zijn gemaakt
    print ("States stored:")
    print (len(room.storage))
    room.show()
    print (len(moveList))


def runSimulationGame4():
    totaal = 0
    room = Board(9, 9)
    carList = []
    freeCars = []
    level = 0
    moveList = []
    
    # red car
    redCar = Car('horizontal', room, 1, 4, 2, 1)
    # Traffic
    traffic1 = Car('vertical', room, 0, 0, 2, 2)
    traffic2 = Car('horizontal', room, 1, 0, 3, 3)
    traffic3 = Car('vertical', room, 6, 0, 3, 5)
    traffic4 = Car('vertical', room, 3, 1, 3, 6)
    traffic5 = Car('horizontal', room, 6, 1, 3, 7)
    traffic6 = Car('vertical', room, 8, 2, 3, 8)
    traffic7 = Car('horizontal', room, 0, 3, 2, 9)
    traffic8 = Car('horizontal', room, 5, 3, 3, 10)
    traffic9 = Car('vertical', room, 0, 4, 2, 11)
    traffic10 = Car('vertical', room, 3, 4, 2, 12)
    traffic11 = Car('vertical', room, 2, 5, 3, 13)
    traffic12 = Car('horizontal', room, 5, 5, 3, 14)
    traffic13 = Car('vertical', room, 8, 5, 3, 15)
    traffic14 = Car('horizontal', room, 0, 6, 2, 16)
    traffic15 = Car('vertical', room, 3, 6, 2, 17)
    traffic16 = Car('horizontal', room, 4, 6, 2, 18)
    traffic17 = Car('vertical', room, 0, 7, 2, 19)
    traffic18 = Car('vertical', room, 4, 7, 2, 20)
    traffic19 = Car('horizontal', room, 1, 8, 3, 21)
    traffic20 = Car('horizontal', room, 5, 8, 2, 22)
    traffic21 = Car('horizontal', room, 7, 8, 2, 23)
    
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12, traffic13, traffic14, \
               traffic15, traffic16, traffic17, traffic18, traffic19, traffic20, traffic21] 
    movesPerLevel = {}
    direction = ''
    counter = 0
    reverseSwitched = False
    winConHor = 5
    winConVer = 2

    while redCar.winCoordinates(winConHor, winConVer) == False:
    # for i in range(0,1):
        reverseSwitched = False
        room.show()
        movesPerLevel[level] = movesPerLevel.get(level, [])
        state = room.convertState()
        # movesPerLevel[level] = movesPerLevel.get(level, [])
        # movesPerLevel2[level] = movesPerLevel2.get(level, [])
        # checker = 0
        # checker2 = 0

        if room.compareState(state) == False:
            room.saveState(state)
            for i in freeCars: 
                i.moved = False
            print ('New state found')
            reverseSwitched = False
        else:
            reverseSwitched = True
            print ('No new state found: ')
            if len(movesPerLevel[level - 1]) == 0:
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                # movesPerLevel[level] = []
                level = level - 2
            else: 
                reverseLastMove(moveList[-1][0],moveList[-1][1])
                moveList.pop()
                level = level - 1       
            room.show()
        
        if len(movesPerLevel[level]) == 0:
            movesPerLevel[level] = []
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    checker3 = 0
                    for i in range(0, len(currentCar.isCarFree())):
                        direction = currentCar.isCarFree()[checker3]
                        movesPerLevel[level].append((currentCar, direction))
                        checker3 += 1

        totaal += len(movesPerLevel[level])

        print (len(movesPerLevel[level]))
        print ("totaal")
        print (totaal)

        # ########## Random version
        randomCar = random.choice(movesPerLevel[level])
        print (randomCar)
        moveCar = randomCar[0]
        print (moveCar)
        print ("Car ID", moveCar.carID, \
                   "It can move to position(s):", moveCar.isCarFree())
        print (randomCar[1])
        moveList.append(randomCar)
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].remove(randomCar)


        # ####### normal version
        # moveCar = (movesPerLevel[level][0][0])
        # print ("Car ID", moveCar.carID, \
        #            "It can move to position(s):", moveCar.isCarFree())
        # print (movesPerLevel[level][0][1])
        # moveList.append(movesPerLevel[level][0])
        # moveCar.move("%s" %moveList[-1][1])
        # movesPerLevel[level].pop(0)    





        level = level + 1
        counter = counter + 1
        print ("Counter: %i" %counter)
        print ("Level: %i" %level)
            
        # maakt freeCars list weer leeg
        freeCars[:] = []

    # toont het aantal unieke states/zetten die zijn gemaakt en
    # de moves die zijn gemaakt
    print ("States stored:")
    print (len(room.storage))
    room.show()
    print (len(moveList))
