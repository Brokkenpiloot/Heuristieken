# Heuristieken.
# Joost Jason en Joren.
# RushHour. 

import random
import timeit
import matplotlib.pyplot as plt

# Bord object waarop autos geplaatst kunnen worden.
class Board(object):

    # Initializer, vergt twee afmeting integers, waar vervolgens een list of lists mee gemaakt wordt.
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.tiles = [["empty" for i in range(width)] for j in range(height)]
        self.storage = set()

    # Print het bord, waarbij "empty" een lege tile en "Car x" een auto voorstelt.
    def show(self):
        for row in self.tiles:
            print(row)

    # Voegt een verticale auto toe aan het bord. Vergt vier integers waarbij x & y de begincoordinaten zijn.
    def addVerticalCar(self, x, y, ID, length): 
        self.tiles[y][x] = 'Car %d' %(ID)
        self.tiles[y+1][x] = 'Car %d' %(ID)
        if length is 3:
            self.tiles[y+2][x] = 'Car %d' %(ID)
            
    # Voegt een horizontale auto toe aan het bord. Vergt vier integers waarbij x & y de begincoordinaten zijn.  
    def addHorizontalCar(self, x, y, ID, length): 
        self.tiles[y][x] = 'Car %d' %(ID)
        self.tiles[y][x+1] = 'Car %d' %(ID)
        if length is 3:
            self.tiles[y][x+2] = 'Car %d' %(ID)

    # Method die checkt of een specifiek coordinaat "empty" is.
    def checkIfEmpty(self, x, y):
        if y >= self.height or x >= self.width:
            return False
        if y < 0 or x < 0:
            return False
        
        if self.tiles[y][x] is 'empty':
            return True
        else:
            return False

    # Method die de waarde van een specifiek coordinaat returned.
    def checkCoordinate(self, x, y):
        print(self.tiles[y][x])

    # Zet het bord (in een list of lists formaat) om in een string.    
    def convertState(self):
        state = ''
        for i in range(self.height):
            state = state + ''.join(self.tiles[i])
        return state
    
    # Voegt state string toe aan set storage.
    def saveState(self, state):
        self.storage.add(state)

    # Zoekt of state string bestaat in set, returnt true indien ja.
    def compareState(self, state):
        return state in self.storage

# Auto object, welke op een reeds bestaand bord geplaatst kunnen worden.
class Car(object):

    # Initializer die een auto met alle relevante eigenschappen aanmaakt.
    def __init__(self, orientation, board, x, y, length, carID):
        self.orientation = orientation
        self.board = board
        self.x = x
        self.y = y
        self.length = length
        self.carID = carID

        # Deel van de initializer. Zorgt dat de auto op het bord op de juiste manier geplaatst wordt.
        if orientation is 'horizontal':
            board.addHorizontalCar(x, y, carID, self.length)
        if orientation is 'vertical':
            board.addVerticalCar(x, y, carID, self.length)

    # Method die checkt of een auto bewegingsruimte heeft. Heeft twee versies, voor horizontal en vertical.
    def isCarFree(self):

        # De versie voor horizontale autos.
        if self.orientation is 'horizontal':
            if self.x - 1 < 0 and self.x + self.length >= self.board.width:
                return ['']

            # Returned de relevante waarden.
            if self.board.checkIfEmpty(self.x - 1, self.y) and \
            self.board.checkIfEmpty(self.x + self.length, self.y):
                return ['left', 'right']

            elif self.board.checkIfEmpty(self.x - 1, self.y):
                return  ['left']

            elif self.board.checkIfEmpty(self.x + self.length, self.y):
                return ['right']
            else:
                return ['']

        # De versie voor verticale autos.
        if self.orientation is 'vertical':
            if self.y - 1 < 0 and self.y + self.length >= self.board.height:
                return ['']

            # Returnt de relevante waarden.
            if self.board.checkIfEmpty(self.x, self.y - 1) and \
            self.board.checkIfEmpty(self.x, self.y + self.length):
                return ['top', 'bot']

            elif self.board.checkIfEmpty(self.x, self.y - 1):
                return ['top'] 

            elif self.board.checkIfEmpty(self.x, self.y + self.length):
                return ['bot']

            else:
                return ['']

    # Method die een auto op het bord verzet in de meegegeven direction.
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

    # Checkt of het rode autotje in positie is om te winnen. Relevante coordinaten moeten meegeleverd worden.
    def winCoordinates(self, x, y):
        if self.board.tiles[self.y][self.x] == self.board.tiles[y][x]:
            return True
        else:
            return False


# Algoritme functie. Dient een game meegeleverd te worden (meer informatie in de readme).
def simulation(room, carList, breakPoint, solutions, winConHor, winConVer):

    # Initialiseerd alle nodige variabelen.
    totaal = 0
    freeCars = []
    level = 0
    moveList = []
    movesPerLevel = {}
    direction = ''
    counter = 0
    reverseSwitched = False
    solutionCounter = 0
    solutionLevels = []
    timeList = []
    start_time = timeit.default_timer()

    #
    while solutionCounter < solutions:
        reverseSwitched = False
        movesPerLevel[level] = movesPerLevel.get(level, [])
        state = room.convertState()

        #
        if room.compareState(state) == False and level < breakPoint:
            room.saveState(state)                       
            for i in freeCars: 
                i.moved = False
            reverseSwitched = False
        elif level == 0:
            for i in freeCars: 
                i.moved = False
            reverseSwitched = False            
        else:
            reverseSwitched = True
            for i in range(len(movesPerLevel)):
                if level == 0:
                    print ("went back to start")
                    break
                
                # Gaat terug zolang hij geen level vindt waar nog mogelijke moves op staan.
                if len(movesPerLevel[level - 1]) == 0:
                    reverseLastMove(moveList[-1][0], moveList[-1][1])
                    moveList.pop()
                    level = level - 1
                elif len(movesPerLevel[level - 1]) > 0:
                    reverseLastMove(moveList[-1][0], moveList[-1][1])
                    moveList.pop()
                    level = level - 1
                    break
                
        # Kleine bugfix voor een in uitzonderlijke gevallen voorkomende bug.
        if level == 0 and counter > 50:
            break

        # Wanneer een nieuw niveau bereikt wordt, maakt deze functie een
        # lijst van mogelijke zetten aan.
        if len(movesPerLevel[level]) == 0:
            movesPerLevel[level] = []
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    checker3 = 0
                    for i in range(0, len(currentCar.isCarFree())):
                        direction = currentCar.isCarFree()[checker3]
                        movesPerLevel[level].append((currentCar, direction))
                        checker3 += 1
        totaal += len(movesPerLevel[level])

        # Random version.
        randomCar = random.choice(movesPerLevel[level])
        moveCar = randomCar[0]
        moveList.append(randomCar)
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].remove(randomCar)

        
        """
        # Normal version.
        moveCar = (movesPerLevel[level][0][0])
        print ("Car ID", moveCar.carID, "It can move to position(s):", moveCar.isCarFree())
        moveList.append(movesPerLevel[level][0])
        moveCar.move("%s" %moveList[-1][1])
        movesPerLevel[level].pop(0)
        """   

        # Update de beide tracker variabelen.
        level = level + 1
        counter = counter + 1 
            
        # Maakt freeCars list weer leeg.
        freeCars[:] = []
        currentTime = (timeit.default_timer() - start_time)
        if currentTime > 1800.0:
            timeList.append(timeit.default_timer() - start_time)
            print ("No new states found for 30 minutes")
            break
            
        # 
        if carList[0].winCoordinates(winConHor, winConVer) == True and level < breakPoint:
            timeList.append(timeit.default_timer() - start_time)        
            print("Runtime:", timeit.default_timer() - start_time)
            solutionCounter = solutionCounter + 1
            solutionLevels.append(level)
            breakPoint = level          
            room.show()
            start_time = timeit.default_timer()            
            print ("Counter: %i" %counter)
            print ("Level: %i" %level)

            

    # Toont informatie over de run op het scherm.
    print ("States stored:")
    print (len(room.storage))
    room.show()
    print (len(moveList))
    
    return [counter, solutionLevels, timeList]
    
        
# Wanneer een zet niet tot een nieuwe staat leidt kan die zet met deze functie reversed worden.
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

# Checkt alle mogelijke zetten, dus inclusief auto's die aan beide kanten vrij staan.
def possibleMoves(): 
    if len(movesPerLevel[level]) == 0:
            print ("moves per level leeg")
            for currentCar in carList:
                if currentCar.isCarFree()[0] != '':
                    freeCars.append(currentCar)
                    for direction in currentCar.isCarFree():
                        movesPerLevel[level].append((currentCar, direction))

# Functie die het algoritme meerdere keren en met backtracking kan runnen.
# Kan daarbij de relevante informatie tonen en plotten.
def timer(simulation, numberOfLoops, breakPoint):

    # Initialiseerd alle nodige variabelen.
    moveCountList = []
    levelCountList = []
    returnValues = []
    timeList = []
    moveCount = 0
    runCounter = []
    solutions = int(raw_input("Number of solutions?: "))

    #
    for i in range(numberOfLoops):    
        returnValues = simulation(breakPoint, solutions)
        moveCount = returnValues[0]
        solutionLevels = returnValues[1]
        moveCountList.append(moveCount)
        timeList.extend(returnValues[2])
        levelCountList.extend(solutionLevels)
        breakPoint = levelCountList[-1]        
        print("Moves:", moveCount)

    # Toont de lengte van de kortst gevonden route als er een route gevonden is.
    avgMoves = sum(moveCountList) / len(moveCountList)
    print ("Average amount of moves used:", avgMoves)
    if len(levelCountList) > 0:
        print ("Shortest routes: ", levelCountList)
    else:
        print ("No solutions found")
        
    # Print counters.
    for i in range(0, len(levelCountList)):
        runCounter.append(i)
    print(len(levelCountList))
    print(len(runCounter))
    
    # Plot data mbv PyPlot.
    radius = runCounter
    area = levelCountList
    plt.plot(radius, area)
    topLimit = levelCountList[0]
    topLimit = topLimit * 1.1
    bottomLimit = levelCountList[-1]
    bottomLimit = bottomLimit * 0.9
    plt.xlabel('Aantal Oplossingen')
    plt.ylabel('Lengte Oplossing')
    plt.title('Game 7')
    plt.ylim((bottomLimit, topLimit))
    plt.xlim((0, len(runCounter)))
    plt.legend()
    plt.show()

    # Alternatieve plots.
    """
    for i in range(0, len(timeList)):
        runCounter.append(i)
    radius = runCounter
    area = timeList
    plt.plot(radius, area)
    plt.xlabel('Aantal Oplossingen')
    plt.ylabel('Tijd in Seconden')
    plt.title('Game 7')
    plt.xlim((0, len(runCounter)))
    plt.legend()
    plt.show()
    """    
    
    
# 7 predefined boards.
def game1(breakPoint, solutions):

    room = Board(6, 6)
    winConHor = 5
    winConVer = 2
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
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)

      
def game2(breakPoint, solutions):

    room = Board(6, 6)
    winConHor = 5
    winConVer = 2
    redCar = Car('horizontal', room, 2, 2, 2, 1)
    
    # Traffic
    traffic1 = Car('horizontal', room, 2, 0, 2, 2)
    traffic2 = Car('horizontal', room, 4, 0, 2, 3)
    traffic3 = Car('horizontal', room, 1, 1, 2, 4)
    traffic4 = Car('horizontal', room, 3, 1, 2, 5)
    traffic5 = Car('vertical', room, 5, 1, 3, 6)
    traffic6 = Car('vertical', room, 4, 2, 2, 7)
    traffic7 = Car('horizontal', room, 0, 3, 2, 8)
    traffic8 = Car('horizontal', room, 2, 3, 2, 9)
    traffic9 = Car('vertical', room, 0, 4, 2, 10)
    traffic10 = Car('vertical', room, 3, 4, 2, 11)
    traffic11 = Car('horizontal', room, 4, 4, 2, 12)
    traffic12 = Car('horizontal', room, 4, 5, 2, 13)
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12] 
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)

def game3(breakPoint, solutions):
    
    room = Board(6, 6)
    winConHor = 5
    winConVer = 2
    redCar = Car('horizontal', room, 0, 2, 2, 1)
    
    # Traffic
    traffic1 = Car('horizontal', room, 1, 0, 2, 2)
    traffic2 = Car('horizontal', room, 3, 0, 3, 3)
    traffic3 = Car('horizontal', room, 1, 1, 2, 4)
    traffic4 = Car('vertical', room, 3, 1, 2, 5)
    traffic5 = Car('horizontal', room, 4, 1, 2, 6)
    traffic6 = Car('vertical', room, 2, 2, 2, 7)
    traffic7 = Car('vertical', room, 5, 2, 2, 8)
    traffic8 = Car('horizontal', room, 0, 3, 2, 9)
    traffic9 = Car('horizontal', room, 3, 3, 2, 10)
    traffic10 = Car('vertical', room, 0, 4, 2, 11)
    traffic11 = Car('vertical', room, 2, 4, 2, 12)
    traffic12 = Car('horizontal', room, 4, 4, 2, 13)
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12]
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)
    


def game4(breakPoint, solutions):

    room = Board(9, 9)
    winConHor = 8
    winConVer = 4
    redCar = Car('horizontal', room, 1, 4, 2, 1)
    
    # Traffic
    traffic1 = Car('vertical', room, 0, 0, 2, 2)
    traffic2 = Car('horizontal', room, 1, 0, 3, 3)
    traffic3 = Car('vertical', room, 5, 0, 3, 4)
    traffic4 = Car('vertical', room, 3, 1, 3, 5)
    traffic5 = Car('horizontal', room, 6, 1, 3, 6)
    traffic6 = Car('vertical', room, 8, 2, 3, 7)
    traffic7 = Car('horizontal', room, 0, 3, 2, 8)
    traffic8 = Car('horizontal', room, 5, 3, 3, 9)
    traffic9 = Car('vertical', room, 0, 4, 2, 10)
    traffic10 = Car('vertical', room, 3, 4, 2, 11)
    traffic11 = Car('vertical', room, 2, 5, 3, 12)
    traffic12 = Car('horizontal', room, 5, 5, 3, 13)
    traffic13 = Car('vertical', room, 8, 5, 3, 14)
    traffic14 = Car('horizontal', room, 0, 6, 2, 15)
    traffic15 = Car('vertical', room, 3, 6, 2, 16)
    traffic16 = Car('horizontal', room, 4, 6, 2, 17)
    traffic17 = Car('vertical', room, 0, 7, 2, 18)
    traffic18 = Car('vertical', room, 4, 7, 2, 19)
    traffic19 = Car('horizontal', room, 1, 8, 3, 20)
    traffic20 = Car('horizontal', room, 5, 8, 2, 21)
    traffic21 = Car('horizontal', room, 7, 8, 2, 22)
    
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12, traffic13, traffic14, \
               traffic15, traffic16, traffic17, traffic18, traffic19, traffic20, traffic21] 
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)

def game5(breakPoint, solutions):

    room = Board(9, 9)
    winConHor = 8
    winConVer = 4
    redCar = Car('horizontal', room, 6, 4, 2, 1)
    
    # Traffic
    traffic1 = Car('horizontal', room, 0, 0, 3, 2)
    traffic2 = Car('vertical', room, 3, 0, 3, 3)
    traffic3 = Car('vertical', room, 5, 0, 2, 4)
    traffic4 = Car('vertical', room, 6, 0, 2, 5)
    traffic5 = Car('horizontal', room, 7, 1, 2, 6)
    traffic6 = Car('horizontal', room, 4, 2, 2, 7)
    traffic7 = Car('vertical', room, 6, 2, 2, 8)
    traffic8 = Car('horizontal', room, 4, 3, 2, 9)
    traffic9 = Car('horizontal', room, 7, 3, 2, 10)
    traffic10 = Car('horizontal', room, 2, 4, 3, 11)
    traffic11 = Car('vertical', room, 5, 4, 3, 12)
    traffic12 = Car('horizontal', room, 6, 4, 2, 13)
    traffic13 = Car('vertical', room, 8, 4, 3, 14)
    traffic14 = Car('vertical', room, 0, 5, 2, 15)
    traffic15 = Car('vertical', room, 2, 5, 2, 16)
    traffic16 = Car('horizontal', room, 3, 6, 2, 17)
    traffic17 = Car('horizontal', room, 6, 6, 2, 18)
    traffic18 = Car('vertical', room, 0, 7, 2, 19)
    traffic19 = Car('vertical', room, 1, 7, 2, 20)
    traffic20 = Car('horizontal', room, 2, 7, 2, 21)
    traffic21 = Car('vertical', room, 4, 7, 2, 22)
    traffic22 = Car('horizontal', room, 5, 7, 3, 23)
    traffic23 = Car('vertical', room, 8, 7, 2, 24)
    traffic24 = Car('horizontal', room, 2, 8, 2, 25)
    
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12, traffic13, traffic14, \
               traffic15, traffic16, traffic17, traffic18, traffic19, traffic20, traffic21, \
               traffic22, traffic23, traffic24]
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)
    


def game6(breakPoint, solutions):

    room = Board(9, 9)
    winConHor = 8
    winConVer = 4
    redCar = Car('horizontal', room, 0, 4, 2, 1)
    
    # Traffic
    traffic1 = Car('horizontal', room, 0, 0, 2, 2)
    traffic2 = Car('horizontal', room, 2, 0, 2, 3)
    traffic3 = Car('vertical', room, 4, 0, 2, 4)
    traffic4 = Car('vertical', room, 7, 0, 2, 5)
    traffic5 = Car('vertical', room, 0, 1, 2, 6)
    traffic6 = Car('horizontal', room, 1, 1, 3, 7)
    traffic7 = Car('horizontal', room, 5, 1, 2, 8)
    traffic8 = Car('horizontal', room, 2, 2, 2, 9)
    traffic9 = Car('vertical', room, 4, 2, 2, 10)
    traffic10 = Car('vertical', room, 5, 2, 2, 11)
    traffic11 = Car('horizontal', room, 7, 2, 2, 12)
    traffic12 = Car('vertical', room, 2, 3, 2, 13)
    traffic13 = Car('vertical', room, 3, 3, 3, 14)
    traffic14 = Car('horizontal', room, 6, 3, 3, 15)
    traffic15 = Car('vertical', room, 1, 5, 2, 16)
    traffic16 = Car('horizontal', room, 4, 5, 2, 17)
    traffic17 = Car('horizontal', room, 6, 5, 2, 18)
    traffic18 = Car('vertical', room, 8, 5, 3, 19)
    traffic19 = Car('vertical', room, 0, 6, 3, 20)
    traffic20 = Car('horizontal', room, 2, 6, 2, 21)
    traffic21 = Car('vertical', room, 4, 6, 3, 22)
    traffic22 = Car('horizontal', room, 5, 6, 3, 23)
    traffic23 = Car('horizontal', room, 2, 7, 2, 24)
    traffic24 = Car('horizontal', room, 5, 7, 2, 25)
    traffic25 = Car('horizontal', room, 1, 8, 3, 26)
    
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12, traffic13, traffic14, \
               traffic15, traffic16, traffic17, traffic18, traffic19, traffic20, traffic21, \
               traffic22, traffic23, traffic24, traffic25] 
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)

def game7(breakPoint, solutions):

    room = Board(12, 12)
    winConHor = 11
    winConVer = 5
    redCar = Car('horizontal', room, 2, 5, 2, 1)
    
    # Traffic
    traffic1 = Car('vertical', room, 0, 0, 2, 2)
    traffic2 = Car('vertical', room, 6, 0, 2, 3)
    traffic3 = Car('horizontal', room, 7, 0, 3, 4)
    traffic4 = Car('horizontal', room, 10, 0, 2, 5)
    traffic5 = Car('vertical', room, 5, 1, 2, 6)
    traffic6 = Car('vertical', room, 10, 1, 2, 7)
    traffic7 = Car('vertical', room, 11, 1, 2, 8)
    traffic8 = Car('horizontal', room, 0, 2, 3, 9)
    traffic9 = Car('horizontal', room, 3, 2, 2, 10)
    traffic10 = Car('vertical', room, 6, 2, 3, 11)
    traffic11 = Car('horizontal', room, 7, 2, 2, 12)
    traffic12 = Car('vertical', room, 0, 3, 3, 13)
    traffic13 = Car('vertical', room, 1, 3, 3, 14)
    traffic14 = Car('vertical', room, 5, 3, 2, 15)
    traffic15 = Car('horizontal', room, 7, 3, 2, 16)
    traffic16 = Car('horizontal', room, 9, 3, 2, 17)
    traffic17 = Car('horizontal', room, 2, 4, 3, 18)
    traffic18 = Car('horizontal', room, 7, 4, 3, 19)
    traffic19 = Car('vertical', room, 4, 5, 2, 20)
    traffic20 = Car('vertical', room, 5, 5, 2, 21)
    traffic21 = Car('horizontal', room, 0, 6, 3, 22)
    traffic22 = Car('vertical', room, 3, 6, 2, 23)
    traffic23 = Car('vertical', room, 6, 6, 3, 24)
    traffic24 = Car('vertical', room, 7, 6, 2, 25)
    traffic25 = Car('vertical', room, 9, 6, 2, 26)
    traffic26 = Car('horizontal', room, 10, 6, 2, 27)
    traffic27 = Car('horizontal', room, 0, 7, 3, 28)
    traffic28 = Car('horizontal', room, 4, 7, 2, 29)
    traffic29 = Car('horizontal', room, 10, 7, 2, 30)
    traffic30 = Car('horizontal', room, 0, 8, 2, 31)
    traffic31 = Car('vertical', room, 2, 8, 2, 32)
    traffic32 = Car('horizontal', room, 3, 8, 3, 33)
    traffic33 = Car('horizontal', room, 7, 8, 3, 34)
    traffic34 = Car('vertical', room, 11, 8, 2, 35)
    traffic35 = Car('horizontal', room, 3, 9, 3, 36)
    traffic36 = Car('vertical', room, 6, 9, 3, 37)
    traffic37 = Car('horizontal', room, 8, 9, 2, 38)
    traffic38 = Car('vertical', room, 10, 9, 3, 39)
    traffic39 = Car('vertical', room, 9, 10, 2, 40)
    traffic40 = Car('vertical', room, 11, 10, 2, 41)
    traffic41 = Car('horizontal', room, 1, 11, 2, 42)
    traffic42 = Car('horizontal', room, 3, 11, 3, 43)
    traffic43 = Car('horizontal', room, 7, 11, 2, 44)
    
    
    carList = [redCar, traffic1, traffic2, traffic3, traffic4, traffic5, traffic6, traffic7, \
               traffic8, traffic9, traffic10, traffic11, traffic12, traffic13, traffic14, \
               traffic15, traffic16, traffic17, traffic18, traffic19, traffic20, traffic21, \
               traffic22, traffic23, traffic24, traffic25, traffic26, traffic27, traffic28, \
               traffic29, traffic30, traffic31, traffic32, traffic33, traffic34, traffic35, \
               traffic36, traffic37, traffic38, traffic39, traffic40, traffic41, traffic42, \
               traffic43]
    return simulation(room, carList, breakPoint, solutions, winConHor, winConVer)
