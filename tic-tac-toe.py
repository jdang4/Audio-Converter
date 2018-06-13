#!/usr/bin/python3.6

board = {'T.L': ' ', 'T.M': ' ', 'T.R' : ' ',
         'M.L': ' ', 'M.M': ' ', 'M.R' : ' ',
         'B.L': ' ', 'B.M': ' ', 'B.R': ' '};

usedPositions = [];
error = False;
availableKeys = [];

for key in board.keys() :
	availableKeys.append(key);

####################################################################################################
#################################### DEFINING THE FUNCTIONS ########################################

def printB(position) :
	
	print ("");
	print ("| " + board['T.L'] + " | " + board['T.M'] + " | " + board['T.R'] + " |");
	print (("------" * 2) + "-");
	print ("| " + board['M.L'] + " | " + board['M.M'] + " | " + board['M.R'] + " |");
	print (("------" * 2) + "-");
	print ("| " + board['B.L'] + " | " + board['B.M'] + " | " + board['B.R'] + " |");
	print ("");

def userX() :
	global error;
	print(", ".join(['{0}'.format(key) for key in availableKeys]));

	print("");	
	user = input('Enter which of the positions above that you want to use: ').upper();

	if ((user not in board.keys()) or (user in usedPositions)) :
		print("Either that position is not available or it was used. Choose again");
		print("");
		error = True;

	else :
		board[user] = 'X';
		usedPositions.append(user);
		error = False;
		if (user in availableKeys) :
			availableKeys.remove(user);


def userO() :
	global error;
	print(", ".join(['{0}'.format(key) for key in availableKeys]));

	print("");	
	user = input("Enter which of the positions above that you want to use: ").upper();

	if ((user not in board.keys()) or (user in usedPositions)) :
		print("Either that position is not available or it was used. Choose again");
		print("");
		error = True;

	else :
		board[user] = 'O';
		usedPositions.append(user);
		error = False;
		if (user in availableKeys) :
			availableKeys.remove(user);

def horizontal(i) :
	if ((board.get("T.L") == i) and (board.get("T.M") == i) and (board.get("T.R") == i)) :
		return True;

	if ((board.get("M.L") == i) and (board.get("M.M") == i) and (board.get("M.R") == i)) :
		return True;

	if ((board.get("B.L") == i) and (board.get("B.M") == i) and (board.get("B.R") == i)) :
		return True;


def vertical(i) :
	if ((board.get("T.L") == i) and (board.get("M.L") == i) and (board.get("B.L") == i)) :
		return True;

	if ((board.get("T.M") == i) and (board.get("M.M") == i) and (board.get("B.M") == i)) :
		return True;

	if ((board.get("T.R") == i) and (board.get("M.R") == i) and (board.get("B.R") == i)) :
		return True;


def diagonal(i) :
	if ((board.get("T.L") == i) and (board.get("M.M") == i) and (board.get("B.R") == i)) :
		return True;

	if ((board.get("T.R") == i) and (board.get("M.M") == i) and (board.get("B.L") == i)) :
		return True;


def checker(i) :
	if (horizontal(i) or vertical(i) or diagonal(i)) :
		return True;
	else :
		return False;

def main() :
	count = 1;
	while(count < 10) :
		
		while(True) :
			printB(board);
			print("It is User 1's turn");
			userX();
			if (error == False) :
				break;

		print("");

		if (checker('X')) :
			printB(board);
			print("Game Over. User 1 won");
			break;


		count += 1;
		if (count == 6) :
			printB(board);
			print("Game Over. No one won");
			break;

		while(True) :
			printB(board);
			print("It is User 2's turn");
			userO();
			if (error == False) :
				break;
		
		print("");

		if (checker('O')) :
			printB(board);
			print("Game Over. User 2 won");
			break;
 
####################################################################################################
#################################### ACTUALLY RUNNING THE PROGRAM ##################################
main();



