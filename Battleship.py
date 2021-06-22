# Function to clear the screen
clear = lambda: print('\n' * 100)

# Class of the playerfields 
class PlayerSea:
    def __init__(self, name):
        self.name = name
        self.privateField = [0 for index in range(419)]
        self.playField = [' ⛋ ' for index in range(419)]

    def setPrivateField(self, fieldIndexes):
        for index in fieldIndexes:
            self.privateField[index] = 1

    def setPlayField(self, fieldIndex, isHit):
        if isHit: 
            self.playField[fieldIndex] = ' ⛝ '
        else:
            self.playField[fieldIndex] = ' ⛞ '
    
    def showPlayField(self, isPlayField):
        fieldIndex = 0
        columnCounter = 0

        rowIndexes = ''
        boardOutput = '\n'
        
        field = []
        if isPlayField:
            field = self.playField
        else:
            field = self.privateField
        
        for currentField in field:
            if columnCounter == 0:
                rowIndexes = str(fieldIndex)
                boardOutput+=str(field[fieldIndex])
                columnCounter+=1
                fieldIndex+=1 
                
            elif columnCounter < 19:
                boardOutput+=str(field[fieldIndex])
                columnCounter+=1
                fieldIndex+=1 
            elif columnCounter == 19:
                boardOutput+=str(field[fieldIndex])
                columnCounter+=1
            else:
                rowIndexes+=f'-{fieldIndex}'
                boardOutput+=f'  [{rowIndexes}] \n'
                columnCounter = 0
                rowIndexes = 0
                fieldIndex+=1 

                 
            
        rowIndexes+=f'-{fieldIndex}'
        boardOutput+=f'  [{rowIndexes}] \n'
        print(boardOutput)

    def shipPlacementPosition(self, currentShip):
        placementPosition = 0
        self.showPlayField(False)
        
        while True:
            placementPosition = int(input(f'Give a position for {currentShip.name} [0-399] : '))
            if placementPosition >= 0 and placementPosition <= 399:
                self.shipPlacementRotation(currentShip, placementPosition)
                break
            else:
                print('Wrong input, try again')
                continue
            
        

    def shipPlacementRotation(self, currentShip, placementPosition):
        placementRotation = ''
        while True: 
            placementRotation = input('Do you want to place your boat horizontal or vertical? (H/V) : ')
            
            if placementRotation.upper() == 'H':
                shipSize = placementPosition + (currentShip.size - 1)
                if ((placementPosition >= 0 and placementPosition <= 19) and shipSize <= 19) or ((placementPosition >= 20 and placementPosition <= 39) and shipSize <= 39) or ((placementPosition >= 40 and placementPosition <= 59) and shipSize <= 59) or ((placementPosition >= 60 and placementPosition <= 79) and shipSize <= 79) or ((placementPosition >= 80 and placementPosition <= 99) and shipSize <= 99) or ((placementPosition >= 100 and placementPosition <= 119) and shipSize <= 119) or ((placementPosition >= 120 and placementPosition <= 139) and shipSize <= 139) or ((placementPosition >= 140 and placementPosition <= 149) and shipSize <= 149) or ((placementPosition >= 160 and placementPosition <= 179) and shipSize <= 179) or ((placementPosition >= 180 and placementPosition <= 199) and shipSize <= 199) or ((placementPosition >= 200 and placementPosition <= 219) and shipSize <= 219) or ((placementPosition >= 220 and placementPosition <= 239) and shipSize <= 239) or ((placementPosition >= 240 and placementPosition <= 259) and shipSize <= 259) or ((placementPosition >= 260 and placementPosition <= 279) and shipSize <= 279) or ((placementPosition >= 280 and placementPosition <= 299) and shipSize <= 299) or ((placementPosition >= 300 and placementPosition <= 319) and shipSize <= 319) or ((placementPosition >= 320 and placementPosition <= 339) and shipSize <= 339) or ((placementPosition >= 340 and placementPosition <= 359) and shipSize <= 359) or ((placementPosition >= 360 and placementPosition <= 379) and shipSize <= 379) or ((placementPosition >= 380 and placementPosition <= 399) and shipSize <= 399):
                    shipIndexes = []
                    position = placementPosition 
                    for size in range(currentShip.size):
                        shipIndexes.append(position)
                        position+=1
                    self.setPrivateField(shipIndexes)
                    break
                else:
                    userInput = input('Not possible at this position, press enter to try again or (R) to choose another position : ')
                    if userInput.upper() == 'R':
                        self.shipPlacementPosition(currentShip)
                        break
                    else:
                        continue
                    
            elif placementRotation.upper() == 'V':
                shipSize = placementPosition + ((currentShip.size-1)*20)
                if shipSize <= 399:
                    shipIndexes = []
                    position = placementPosition
                    for size in range(currentShip.size):
                        shipIndexes.append(position)
                        position+=20
                    self.setPrivateField(shipIndexes)
                    break
                else:
                    userInput = input('Not possible at this position, press enter to try again or (R) to choose another position : ')
                    if userInput.upper() == 'R':
                        self.shipPlacementPosition(currentShip)
                        break
                    else:
                        continue

            else:
                print('Wrong input, try again')
                continue
    
    def checkShot(self, fieldIndex):
        if self.privateField[fieldIndex] == 1:
            playField(fieldIndex, True)
            print('HIT!\n')
            return True
        else:
            playField(fieldIndex, False)
            print('MISS!\n')
            return False
    
# Head class of the ships
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []

    def getName():
        print(f'This ship is a {name}')
        
    def getCoordinates():
        print(coordinates)

# Class of the Patrol Ship
class Patrol(Ship):
    def setCoordinates():
        print('TBA')

# Class of the Cruiser Ship
class Cruiser(Ship):
    def setCoordinates():
        print('TBA')

# Class of the Aircraft Carrier
class AircraftCarrier(Ship):
    def setCoordinates():
        print('TBA')

# Function that manages the main menu
def mainMenu():
    while True:
        clear()
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
    shipsPlayerOne = [Patrol('Patrol Ship', 2), Patrol('Patrol Ship', 2), Cruiser('Cruiser', 3), Cruiser('Cruiser', 3), AircraftCarrier('Aircraft Carrier', 4), AircraftCarrier('Aircraft Carrier', 4)]
    shipsPlayerTwo = shipsPlayerOne #test

    clear()
    
    print('******** LOCAL VERSUS ********\n\n')
    seaName = input('Player One, give your part of the sea a name: ')
    playBoardOne = PlayerSea(seaName)

    seaName = input('\nPlayer Two, give your part of the sea a name: ')
    playBoardTwo = PlayerSea(seaName)

    clear()
    
    # Player One ship placement
    print(f'******** Player One, place your boats for {playBoardOne.name} ********\n')
    placementIndex = 0
    while placementIndex < 6:
        playBoardOne.shipPlacementPosition(shipsPlayerOne[placementIndex])
        placementIndex += 1

    playBoardOne.showPlayField(False)
    input('Press enter to continue ')

    clear()
    
    # Player Two ship placement
    print(f'******** Player Two, place your boats for {playBoardTwo.name} ********')
    placementIndex = 0
    while placementIndex < 6:
        playBoardTwo.shipPlacementPosition(shipsPlayerTwo[placementIndex])
        placementIndex += 1

    playBoardTwo.showPlayField(False)
    input('Press enter to continue ')

    # Start the game
    #localVersusPlay([playBoardOne, playBoardTwo],[shipsPlayerOne, shipsPlayerTwo])

# Function that manages the gameplay
def localVersusPlay(boards, ships):
    clear()
    print('TBA')




mainMenu()



