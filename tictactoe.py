import random
import time

keepplaying = True
separator = "-------"
example = " 1|2|3\n-------\n 4|5|6\n-------\n 7|8|9"

print "\n\nHello and welcome to Ryan's Tic Tac Toe game, coded in Python!"

print example

print "This is how the game works. I will prompt the respective player to pick where to put their symbol. Player 1 places 'X's and Player 2 places 'O's. Standard rules apply. The player order is assigned at random. Enjoy!"

player1 = raw_input("Please enter a player's name.: ")
player2 = raw_input("Please enter the other player's name.: ")

while keepplaying:
	#this determines the player order
	player_order = [1,2]
	random.seed(time.time())
	firstplayer = random.randint(1,2)
	if (firstplayer == 2):
		player_order = [2,1]
	
	#keeps track of game progress
	gameboard = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "} #keeps track of wich positions have already been used in the game
	currentplayer = player_order[0]	#Sets the selected first player as the first player in the game. Determines who's turn it is right now.
	usedspaces = [] #Keeps track of which spaces have already been used in the game. Prevents a player from overwriting a space with a mark already in it.

	#prints the current state of the game board
	def printboard():
		print " " + gameboard[1] + "|" + gameboard[2] + "|" + gameboard[3]
		print separator
		print " " + gameboard[4] + "|" + gameboard[5] + "|" + gameboard[6]
		print separator
		print " " + gameboard[7] + "|" + gameboard[8] + "|" + gameboard[9] + "\n"
	
	#game code is here
	turn = 1
	play = True
	while turn < 10 and play:
		if (currentplayer == player_order[0]): #first player's turn
			nextspace = -1
			#prompt indicating which player's turn it is
                        if(currentplayer == 1):
                                print player1 +  "'s turn!"
                        else:
                                print player2 + "'s turn!"
			while ((nextspace not in range(1,10)) or (nextspace in usedspaces)):
				try:
					nextspace = int(raw_input("Please enter the integer representation of the space you'd like to mark next. Refer to the above illustration with the index numbers.: "))
					if (nextspace in usedspaces):
						print "That space is already in use! Try again."
					elif (nextspace not in range(1,10)):
						print "That is an invalid space number. Try again."
				except ValueError:
					print "Please enter a valid input."
			gameboard[nextspace] = "X"
			usedspaces.append(nextspace)
			print "Ok. Here is the updated game board.:"
			printboard()
			currentplayer = player_order[1]

			#checks if there is a win or not
			#nothing happens if no win, just go to next iteration of while True loop (next player's turn)
			if((gameboard[1] == gameboard[2] and gameboard[2] == gameboard[3] and gameboard[3] == "X") or (gameboard[4] == gameboard[5] and gameboard[5] == gameboard[6]\
 and gameboard[6] == "X") or (gameboard[7] == gameboard[8] and gameboard[8] == gameboard[9] and gameboard[9] == "X") or (gameboard[1] == gameboard[5] and gameboard[5] == gameboard[9]\
 and gameboard[9] == "X") or (gameboard[3] == gameboard[5] and gameboard[5] == gameboard[7] and gameboard[7] == "X") or (gameboard[1] == gameboard[4] and gameboard[4] == gameboard[7]\
 and gameboard[7] == "X") or (gameboard[2] == gameboard[5] and gameboard[5] == gameboard[8] and gameboard[8] == "X") or (gameboard[3] == gameboard[6] and gameboard[6] == gameboard[9]\
 and gameboard[9] == "X")):
				if (currentplayer == 1):
					print player2 + " wins! \n"
				else:
					print player1 + " wins! \n"
				play = False
			turn += 1

		else: #second player's turn
			nextspace = -1
			#prompt indicating which player's turn it is
                        if(currentplayer == 1):
                                print player1 +  "'s turn!"
                        else:
                                print player2 + "'s turn!"
                        while ((nextspace not in range(1,10)) or (nextspace in usedspaces)):
                                try:
					nextspace = int(raw_input("Please enter the integer representation of the space you'd like to mark next. Refer to the above illustration with the index numbers.: "))
        	                        if (nextspace in usedspaces):
                	                        print "That space is already in use! Try again."
					elif (nextspace not in range(1,10)):
						print "That is an invalid space number. Try again."
				except ValueError:
					print "Please enter a valid input."
                        gameboard[nextspace] = "O"
			usedspaces.append(nextspace)
                        print "Ok. Here is the updated game board.:"
                        printboard()
                        currentplayer = player_order[0]

                        #checks if there is a win or not
                        #nothing happens if no win, just go to next iteration of while True loop (next player's turn)
                        if((gameboard[1] == gameboard[2] and gameboard[2] == gameboard[3] and gameboard[3] == "O") or (gameboard[4] == gameboard[5] and gameboard[5] == gameboard[6]\
 and gameboard[6] == "O") or (gameboard[7] == gameboard[8] and gameboard[8] == gameboard[9] and gameboard[9] == "O") or (gameboard[1] == gameboard[5] and gameboard[5] == gameboard[9]\
 and gameboard[9] == "O") or (gameboard[3] == gameboard[5] and gameboard[5] == gameboard[7] and gameboard[7] == "O") or (gameboard[1] == gameboard[4] and gameboard[4] == gameboard[7]\
 and gameboard[7] == "O") or (gameboard[2] == gameboard[5] and gameboard[5] == gameboard[8] and gameboard[8] == "O") or (gameboard[3] == gameboard[6] and gameboard[6] == gameboard[9]\
 and gameboard[9] == "O")):
                                if (currentplayer == 2):
                                        print player1 + " wins! \n"
				else:
					print player2 + " wins! \n"
                                play = False
			turn += 1

	#End of a game. Prompts if either to keep playing or exit program.
	isvalid = "abc"
	while (isvalid.lower() != "yes" and isvalid.lower() != "no"):
		isvalid = raw_input("Would you like to keep playing? Please say 'Yes' if you would. Otherwise type 'No'.: ")
	if(isvalid.lower() == "no"):
		keepplaying = False

	if (keepplaying):
		namechange = "abc"
		while (namechange.lower() != "yes" and namechange.lower() != "no"):
			namechange = raw_input("Would you like to change the player names? Please say either 'Yes' or 'No'.: ")
			if (namechange.lower() != "yes" and namechange.lower() != "no"):
				print "Error: please type a valid answer."

		if (namechange.lower() == "yes"):
			player1 = raw_input("Please enter the name of a player.: ")
			player2 = raw_input("Please enter the name of the other player.: ")
		print "\nHere is, once again, how to select which space you want to mark. Just enter the corresponding space number as shown below."
		print example
	
	
else:
	print "Thank you for playing! Goodbye!"
