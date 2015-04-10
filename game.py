# Heuristieken.
# Joost Jason en Joren.
# RushHour.
# 

class Board(object):
    def __init__(self, height, width):
        # Generate empty board as list of lists
        self.height = height
        self.width = width
        self.board = [["empty" for x in range(height)] for count in range(width)]
    def show(self):
        for row in self.board:
            print(row)    
    def addVerticalcar(self, x, y, ID):
        # TODO: create car object 
        
        self.board[x][y] = 'Car %d' %(ID)
        self.board[x+1][y] = 'Car %d' %(ID)
        
    def addHorizontalcar(self, x, y, ID):
        # TODO: create car object 
        
        self.board[x][y] = 'Car %d' %(ID)
        self.board[x][y+1] = 'Car %d' %(ID)
        

# class Car(object):
#     def __init__(self, orientation, board, x, y, length, carID):
#         self.orientation = orientation
#         # Position on board can be called by entering self.board[self.x][self.y]
#         self.board = board
#         self.x = x
#         self.y = y
#         self.length = length
#         self.carID = carID

# Initialize board, pass height en width parameters
# Car ID Integer = 1
# Voeg autos aan bord toe met addCar method en verhoog de car ID integer voor iedere auto 
# Maak car objects aan voor iedere auto (kan misschien binnen addCar method) 

def runSimulationGame1(height, width):

    room = board(width, height)
    # carID = 1

    # addHorizontalCar(x, y, carID, length)
    # red Car
    addHorizontalCar(3, 2, 1, 2)

    # Traffic
    addVerticalCar(2, 0, 2, 3)
    addHorizontalCar(3, 0, 3, 2)
    addVerticalCar(5, 0, 4, 3)
    addVerticalCar(3, 3, 5, 3)
    addHorizontalcar(4, 3, 6, 2)
    addVerticalCar(0, 4, 7, 2)
    addHorizontalCar(1, 4, 8, 2)
    addHorizontalCar(5, 4, 9, 2)   

    room.show()

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


    room.show()

