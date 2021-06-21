class Sea:
    def __init__(self):
        self.field = [" ⛋ " for index in range(419)]

    def showField(self):
        fieldIndex = 0
        columnCounter = 0

        rowIndexes = ""
        boardOutput = ""
        
        for currentField in self.field:
            if columnCounter == 0:
                rowIndexes = str(fieldIndex)
                boardOutput+=self.field[fieldIndex]
                columnCounter+=1
                
            elif columnCounter < 20:
                boardOutput+=self.field[fieldIndex]
                columnCounter+=1

            else:
                rowIndexes+=f"-{fieldIndex}"
                boardOutput+=f"  [{rowIndexes}] \n"
                columnCounter = 0
                rowIndexes = 0

            fieldIndex+=1
            
            
        rowIndexes+=f"-{fieldIndex}"
        boardOutput+=f"  [{rowIndexes}] \n"
        print(boardOutput)


#class SeaPlayerOne(Sea):
    

#class SeaPlayerTwo(Sea):
    

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []

    def getName():
        print(f'This ship is a {name}')
        
    def getCoordinates():
        print(coordinates)
    

class Patrol(Ship):
    def setCoordinates():
        print('TBA')
        
class Cruiser(Ship):
    def setCoordinates():
        print('TBA')

class AircraftCarrier(Ship):
    def setCoordinates():
        print('TBA')

# Function that manages the main menu
def mainMenu():
    while True:
        print('******** BATTLESHIP ********\n\n' +
              '1) Start Local Versus\n' +
              '2) Quit\n')
        userInput = input('Your choice: ')
        if userInput == '1':
            localVersusMenu()
            break
        elif userInput == '2':
            break
        else:
            print('Wrong input, please try again\n')
            continue

# Function that manages the local versus menu
def localVersusMenu():
    print('******** LOCAL VERSUS ********\n\n')
    playBoard = Sea()
    
    shipsPlayerOne = [Patrol('Patrol Boat', 2), Patrol('Patrol Boat', 2), Cruiser('Cruiser', 3), Cruiser('Cruiser', 3), AircraftCarrier('Aircraft Carrier', 4), AircraftCarrier('Aircraft Carrier', 4)]
    shipsPlayerTwo = shipsPlayerOne #test
    
    print('Player One, place your boats')
    placementIndex = 0
    while placementIndex < 6:
        # Todo: Boten plaatsen     
        placementIndex += 1 

def localVersusPlay(boats, board):
    print('TBA')
    
#mainMenu()
playBoard = Sea()
playBoard.showField()
playBoard.field[40] = ' ⛞ '
playBoard.field[30] = ' ⛝ '
playBoard.field[31] = ' ⛝ '
playBoard.field[32] = ' ⛞ '
playBoard.showField()


