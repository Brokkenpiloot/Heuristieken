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
        

class Car(object):
    def __init__(self, orientation, board, x, y, length, carID):
        self.orientation = orientation
        # Position on board can be called by entering self.board[self.x][self.y]
        self.board = board
        self.x = x
        self.y = y
        self.length = length
        self.carID = carID
       
        
    def checkOrientation(self):
        if self.orientation == 0: 
            return horizontal
        elif self.orientation == 1:
            return vertical
        else:
            return 1

    def checkCoordinate(self):
        if (0 <= self.x < width) and (0 <= self.y < height):
            return "X and Y coordinates exist"
        else:
            print self.x
            print self.y
            return 2
    def checkSize(self):
        switch(self.orientation) {
            case 0:
                if self.x + length < width: 
                    return "Car fits on the board (horizontal)"  
            case 1:
                if self.y + length < height: 
                    return "Car fits on the board (vertical)"  
            default:
                return 3
                break;
        }
## Error List:
#   1 = not horizontal or vertical 
#   2 = Car coordinates car do not exist
#   3 = Orientation is not equal to zero or one in Checksize
    





    # Uiteindelijk checks samenvoegen
    # Check toevoegen om te checken of orientation "horizontal" of "vertical" is.
    	# orientation zero = horizontal | one = vertical	
    
    # Check toevoegen of start_coordinate bestaat.
    	# if x and y <= m or n

    # Check toevoegen of start_coordinate + length past in het bord.
    	# if orientation == zero:
    		# check if coordinate x + length <=  m:
    			# return true	
    	#  if orientation == one:
    		# check if coordinate x + length <=  n: 
    			# # return true	 	

    # Check toevoegen of alle in te vullen coordinaten niet al bezet zijn.
    	# for i in (length - x): 
    	# 	if position x i == NULL:
    	# 		return false

# def check(self):
    #     # if horizontal
    #     if self.orientation == 0:
    #         # if start is on the bord 
    #         if 0 <= self.x < height:
    #             # if total size is on the bord
    #             if self.x + length < width:
    #                 return true
    #     # if vertical
    #     elif self.orientation == 1:
    #         # if start is on the bord 
    #         if 0 <= self.y < height:
    #             # if total size is on the bord
    #             if self.y+ length < height:
    #                 return true
    #     else: 
    #         return false

        
