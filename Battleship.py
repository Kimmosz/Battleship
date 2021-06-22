# Function to clear the screen
clear = lambda: print('\n' * 100)

# Function that asks user to press enter to continue
pressEnter = lambda: input('\nPress enter to continue ')

# Class of the playerfields 
class PlayerSea:
    def __init__(self, name):
        self.name = name
        self.privateField = [0 for index in range(419)]
        self.playField = [' ⛋ ' for index in range(419)]
        self.score = 0

    # Function to set the private fields
    def setAllPrivateFields(self, fieldIndexes):
        for index in fieldIndexes:
            self.privateField[index] = 1

    # Function to set the current private field
    def setPrivateField(self, fieldIndex):
        self.privateField[fieldIndex] = 0

    # Function to set the current play field
    def setPlayField(self, fieldIndex, isHit):
        if isHit: 
            self.playField[fieldIndex] = ' ⛝ '
        else:
            self.playField[fieldIndex] = ' ⛞ '

    # Function to show the current private or play field
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

    # Function where player can give a position for the current ship
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
            
        
    # Function where player can place the current ship horizontal or vertical
    def shipPlacementRotation(self, currentShip, placementPosition):
        placementRotation = ''
        while True: 
            placementRotation = input('Do you want to place your boat horizontal or vertical? (H/V) : ')

            # Place ship horizontal
            if placementRotation.upper() == 'H':
                shipSize = placementPosition + (currentShip.size - 1)
                if ((placementPosition >= 0 and placementPosition <= 19) and shipSize <= 19) or ((placementPosition >= 20 and placementPosition <= 39) and shipSize <= 39) or ((placementPosition >= 40 and placementPosition <= 59) and shipSize <= 59) or ((placementPosition >= 60 and placementPosition <= 79) and shipSize <= 79) or ((placementPosition >= 80 and placementPosition <= 99) and shipSize <= 99) or ((placementPosition >= 100 and placementPosition <= 119) and shipSize <= 119) or ((placementPosition >= 120 and placementPosition <= 139) and shipSize <= 139) or ((placementPosition >= 140 and placementPosition <= 149) and shipSize <= 149) or ((placementPosition >= 160 and placementPosition <= 179) and shipSize <= 179) or ((placementPosition >= 180 and placementPosition <= 199) and shipSize <= 199) or ((placementPosition >= 200 and placementPosition <= 219) and shipSize <= 219) or ((placementPosition >= 220 and placementPosition <= 239) and shipSize <= 239) or ((placementPosition >= 240 and placementPosition <= 259) and shipSize <= 259) or ((placementPosition >= 260 and placementPosition <= 279) and shipSize <= 279) or ((placementPosition >= 280 and placementPosition <= 299) and shipSize <= 299) or ((placementPosition >= 300 and placementPosition <= 319) and shipSize <= 319) or ((placementPosition >= 320 and placementPosition <= 339) and shipSize <= 339) or ((placementPosition >= 340 and placementPosition <= 359) and shipSize <= 359) or ((placementPosition >= 360 and placementPosition <= 379) and shipSize <= 379) or ((placementPosition >= 380 and placementPosition <= 399) and shipSize <= 399):
                    shipIndexes = []
                    position = placementPosition 
                    for size in range(currentShip.size):
                        shipIndexes.append(position)                    # Add to Player Sea
                        currentShip.addCoordinate(position)             # Add coordinate to current Ship
                        position+=1
                    self.setAllPrivateFields(shipIndexes)
                    currentShip.getCoordinates()
                    break
                else:
                    userInput = input('Not possible at this position, press enter to try again or (R) to choose another position : ')
                    # Replace position
                    if userInput.upper() == 'R':
                        self.shipPlacementPosition(currentShip)
                        break
                    else:
                        continue

            # Place ship vertical
            elif placementRotation.upper() == 'V':
                shipSize = placementPosition + ((currentShip.size-1)*20)
                if shipSize <= 399:
                    shipIndexes = []
                    position = placementPosition
                    for size in range(currentShip.size):
                        shipIndexes.append(position)                    # Add to Player Sea
                        currentShip.addCoordinate(position)             # Add coordinate to current Ship
                        position+=20
                    self.setAllPrivateFields(shipIndexes)
                    currentShip.getCoordinates()
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

    # Function to check if shot is a hit or a miss
    def checkShot(self, fieldIndex):
        if self.privateField[fieldIndex] != 0:
            self.setPrivateField(fieldIndex)
            self.setPlayField(fieldIndex, True)
            print('HIT!\n')
            pressEnter()
            return True
        else:
            self.setPlayField(fieldIndex, False)
            print('MISS!\n')
            pressEnter()
            return False

    # Function to check if there are ships left
    def shipsLeft(self):
        if 1 in self.privateField:
            return True
        else:
            return False
    
# Head class of the ships
class Ship:
    def __init__(self, shipId, name, size):
        self.shipId = shipId
        self.name = name
        self.size = size
        self.coordinates = []

    def getName():
        print(f'This ship is a {name}')

    def addCoordinate(self, coordinate):
        self.coordinates.append(coordinate)

# Class of the Patrol Ship
class Patrol(Ship):
    def getCoordinates(self):
        print(f'This Patrol Ship is at: {self.coordinates}')
        pressEnter()

# Class of the Cruiser
class Cruiser(Ship):
    def getCoordinates(self):
        print(f'This Cruiser is at: {self.coordinates}')
        pressEnter()

# Class of the Aircraft Carrier
class AircraftCarrier(Ship):
    def getCoordinates(self):
        print(f'This Aircraft Carrier is at: {self.coordinates}')
        pressEnter()

# Function to create new set of ships
createNewShips = lambda: [Patrol(1, 'Patrol Ship', 2), Patrol(2, 'Patrol Ship', 2), Cruiser(3, 'Cruiser', 3), Cruiser(4, 'Cruiser', 3), AircraftCarrier(5, 'Aircraft Carrier', 4), AircraftCarrier(6, 'Aircraft Carrier', 4)]

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
    shipsPlayerOne = createNewShips()
    shipsPlayerTwo = createNewShips()
    
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
    pressEnter()

    clear()
    
    # Player Two ship placement
    print(f'******** Player Two, place your boats for {playBoardTwo.name} ********')
    placementIndex = 0
    while placementIndex < 6:
        playBoardTwo.shipPlacementPosition(shipsPlayerTwo[placementIndex])
        placementIndex += 1

    playBoardTwo.showPlayField(False)
    pressEnter()

    # Start the game
    localVersusPlay([playBoardOne, playBoardTwo],[shipsPlayerOne, shipsPlayerTwo])

# Function that manages the gameplay
def localVersusPlay(boards, ships):
    playerTurn = 0
    while True:
        clear()
        if playerTurn == 0:
            print('******** Turn Player One ********')
            boards[1].showPlayField(True)
            fieldIndex = int(input('Give a number to shoot on [0-399] : '))
            isHit = boards[1].checkShot(fieldIndex)
            isFinished = boards[1].shipsLeft()
            if isHit and not isFinished:
                continue
            elif isHit and isFinished:
                print('***** Player One has won! *****')
                boards[1].showPlayField(True)
                pressEnter()
                mainMenu()
                break
            else:
                playerTurn = 1
                continue
                
        else: 
            print('******** Turn Player Two ********')
            boards[0].showPlayField(True)
            fieldIndex = int(input('Give a number to shoot on [0-399] : '))
            isHit = boards[0].checkShot(fieldIndex)
            shipsLeft = boards[0].shipsLeft()

            if not shipsLeft:
                print('\n***** Player Two has won! *****')
                boards[0].showPlayField(True)
                pressEnter()
                mainMenu()
                break
            
            if isHit:
                continue   
            else:
                playerTurn = 0
                continue


mainMenu()



