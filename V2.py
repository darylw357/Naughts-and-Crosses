#2 Player  Noughts and Crosses Game
import sys, random

#Variable Declairation.

Players = [("Player1",1)] #First player in this list will be the player whose turn it is. if a players turn is over then they are removed and appended to the end.
#Players is a list of tuples, first element name second element symbol to represent player choices.

Grid = [[0,0,0],[0,0,0],[0,0,0]] #Board is laid out as a list of lists so it appears as a 3x3 matrix.

Moves = 0

def OpponentChoiceState():
	Choice = input("[H]uman or [C]omputer opponent ?")
	if Choice == "H":					
		Players.append(("Player2",2))
	elif Choice == "C":
		Players.append(("Computer",3))
	else: 
		print ("Error, Please choose a Human or Computer opponent.")
		return #Exits function and goes back to where it was, loop repeats in this case.
	return PlayerTurnState #State switch.
	

def PrintGrid(): 
	print("--------------")
	for Row in range(len(Grid)):
		for Col in range(len(Grid)):
			Symbol = Grid[Row][Col]
			if Symbol == 1: #Converts player choice into a X or O.
				Symbol = 'X'
			elif Symbol == 0:
				Symbol = '-'
			else:
				Symbol = '0'
			print (Symbol, end=" ") #Argument to make a space at the end.
		print("")
	print("--------------")

def ComputerOpponent(Symbol):
	while True:
		X = random.randint(0, 2) #Random piece allocation on the grid.
		Y = random.randint(0, 2)
		if Grid[X][Y] == 0: #Checks to see if the space is free.
			Grid[X][Y] = Symbol
			break
	print("The computer has made its move.")

def PromptInt(Message): #Catches user errors when a non integer is entered. try is kind of like a virtual machine environment.
	try: # Tests what the user entered.
		Number = int(input(Message)) #Returns verified integer.
		if Number not in range(1,4):
			print ("Position must be between 1 - 3.")
			return PromptInt(Message) #Recursively asks the user for a valid input.
		return Number
	except: #Executed when an error is detected.
		print ("That's not a number.")
		return PromptInt(Message) #Recursively asks the user for a valid input.
		
def PromptPlayerMove():
	print ("Make your move player.")
	X = PromptInt("X: ")-1 #-1 is used because the range is 0-2, however most users will interpret the board as being from 1-3.
	Y = PromptInt("Y: ")-1
	return X,Y
		
def HasPlayerWon(Symbol):
	global Moves
	print (Moves)
	for Row in range(3): #Execute this block of code for each row. Holds true output in PlayerWon.
		PlayerWon = Grid[Row][0] == Symbol and Grid[Row][1] == Symbol and Grid[Row][2] == Symbol # Checks each horizontal, like a AND logic gate, returns true or false.
		PlayerWon = PlayerWon or Grid[0][Row] == Symbol and Grid[1][Row] == Symbol and Grid[2][Row] == Symbol #Checks vertical.
		if PlayerWon: 
			return True
	PlayerWon = Grid[0][0] == Symbol and Grid[1][1] == Symbol and Grid[2][2] == Symbol #Diagonals.
	PlayerWon = PlayerWon or Grid[0][2] == Symbol and Grid[1][1] == Symbol and Grid[2][0] == Symbol #Diagonals.
	if PlayerWon: 
		return Players[0]
	elif Moves == 9:
		return None
	return False	
	
def PlayerTurnState():  
	global Moves
	CurrentPlayer, Symbol = Players[0] #Which is the current player.
	if CurrentPlayer=="Computer":
		ComputerOpponent(Symbol) #Switches to computer opponent function.
	else:
		X,Y = PromptPlayerMove()
		if not Grid[X][Y] == 0:
			print ("That space is already occupied.")
			return
		Grid[X][Y] = Symbol
	PrintGrid()
	Moves += 1 
	print (Moves)
	WinningPlayer = HasPlayerWon(Symbol)
	if not  WinningPlayer == False:
		Players.insert(0,WinningPlayer)
		return GameOverState
	Players.append(Players.pop(0)) #Removes first element from list and adds it to the end of the list. Maybe use players.reverse.
	
def GameOverState():
	if Players[0] == None:
		print ("A Draw.")
	elif Players[0][0] == 'Computer':
		print("The computer wins!")
	else:
		print("{} wins!".format(Players[0][0])) #Outputs the winning player ID. Access list, access tuple.
	input("Press enter to exit.")
	sys.exit(0)

def Main():
	CurrentState = OpponentChoiceState #Initial state is being set to opponent choice state.
	while True:		
		ReturnValue = CurrentState() #Execute current state and save the return value.
		if ReturnValue is not None: #Executed when something is returned.
			CurrentState = ReturnValue #Replaces current state with the state from the return value.
	
if __name__ == '__main__':  #Debug purposes.
	Main()

