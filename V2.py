#Basic 2 Player  Noughts and Crosses Game
import sys, random

Players = [("Player1",1)] #first player in this list will be the player whose turn it is. if a players turn is over then they are removed and appended to the end.
#players is a list of tuples, first element name second element symbol to represent player choices.

Grid = [[0,0,0],[0,0,0],[0,0,0]]

def OpponentChoiceState():
	Choice = input("[H]uman or [C]omputer opponent ?")
	if Choice == "H":					#change state
		Players.append(("Player2",2))
	elif Choice == "C":
		Players.append(("Computer",3))
	else: 
		print ("Level 8 OSI Error")
		return #exits function and goes back to where it was, loop repeats in this case.
	return PlayerTurnState #state switch
	

def PrintGrid():
    print("--------------")
    for Row in range(len(Grid)):
        for Col in range(len(Grid)):
            Symbol = Grid[Row][Col]
            if Symbol == 1:
                Symbol = 'X'
            elif Symbol == 0:
                Symbol = '-'
            else:
                Symbol = '0'
            print (Symbol, end=" ")
        print("")
    print("--------------")

def ComputerOpponent(Symbol):
    while True:
        X = random.randint(0, 2)
        Y = random.randint(0, 2)
        if Grid[X][Y] == 0:
            Grid[X][Y] = Symbol
            break
    print("The computer has made its move.")

def PromptInt(Message): #Catches user errors when a non integer is entered. try is kind of like a virtual machine environment.
	try: # tests what the user entered.
		Number = int(input(Message)) #returns verified integer.
		if Number not in range(1,4):
			print ("Position must be between 1 - 3.")
			return PromptInt(Message) #recursively asks the user for a valid input.
		return Number
	except: #executed when an error is detected.
		print ("That's not a number.")
		return PromptInt(Message) #recursively asks the user for a valid input.
		
def PromptPlayerMove():
    print ("Make your move player.")
    X = PromptInt("X: ")-1# -1 is used because the range is 0-2, however most users will interpret the board as being from 1-3.
    Y = PromptInt("Y: ")-1
    return X,Y
    	
def HasPlayerWon(Symbol):
	  
	for Row in range(3): #execute this block of code for each row.Holds true output in PlayerWon
		PlayerWon = Grid[Row][0] == Symbol and Grid[Row][1] == Symbol and Grid[Row][2] == Symbol # checks each horizontal, AND logic gate, returns true or false
		PlayerWon = PlayerWon or Grid[0][Row] == Symbol and Grid[1][Row] == Symbol and Grid[2][Row] == Symbol# checks vertical
		if PlayerWon: 
			return True
	PlayerWon = Grid[0][0] == Symbol and Grid[1][1] == Symbol and Grid[2][2] == Symbol#diagonals
	PlayerWon = PlayerWon or Grid[0][2] == Symbol and Grid[1][1] == Symbol and Grid[2][0] == Symbol#diagonals
	if PlayerWon: 
		return True
	return False	
	
def PlayerTurnState():  #functions
    CurrentPlayer, Symbol = Players[0] #which player is playing
    if CurrentPlayer=="Computer":
        ComputerOpponent(Symbol)
    else:
        X,Y = PromptPlayerMove()
        if not Grid[X][Y] == 0:
            print ("That space is already occupied.")
            return
        Grid[X][Y] = Symbol
    PrintGrid()
    if HasPlayerWon(Symbol):
        return GameOverState
    Players.append(Players.pop(0)) #removes first element from list and adds it to the end of the list. maybe use players.reverse.
	
def GameOverState():
    if Players[0][0] == 'Computer':
        print("The computer wins!")
    else:
        print("{} wins!".format(Players[0][0]))
    input("Press enter to exit.")
    sys.exit(0)

def Main():
    CurrentState = OpponentChoiceState #state is executed
    while True:		#endless loop really.
        ReturnValue = CurrentState()
        if ReturnValue is not None:
            CurrentState = ReturnValue #switches to previous state in line 45.
	
if __name__ == '__main__':
    Main()

