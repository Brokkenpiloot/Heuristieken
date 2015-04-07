# Heuristieken.
# Joost Jason en Joren.
# RushHour.

class Car(object):
    def __init__(self, orientation, start_coordinate, length):
        self.orientation = orientation
        self.start_coordinate = start_coordinate
        self.length = length

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


        
