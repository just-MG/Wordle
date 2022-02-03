from operator import index
from turtle import clear
import os

def printBoards(allBoards, allGuesses, wrongLetters): # this one is used for printing the outcomes
    a = 0
    for currBoard in allBoards: # looping through each of the answers 
        a += 1
        tmp = ["", "", "", "", ""]
        for i in range(5): # looping through the answers and formatting them to this lil squares
            if currBoard[i] == 0:
                tmp[i] = "⬜"
            elif currBoard[i] == 1:
                tmp[i] = "🟨"
            else:
                tmp[i] = "🟩"
        # printing the outcomes: this monster line below is just for adding a space to each of the letters
        print(str(a) + ": " + str(list(map(lambda x: f"{x} " , list(allGuesses[a-1]))))) #just wanted to add a space :(
        # printing the squares
        print(str(a) + ": " + str(tmp))
    print("wrong letters: " + str(wrongLetters))

def checkIfWon(currBoard):
    # setting the control sum
    sum = 0
    # if the game is won all of the fields are equal to 2 so 2 * 5 = 10
    for each in currBoard:
        sum += int(each) 
    # checking if is equal to 10
    if sum == 10:
        return 1 # if so return that it is a win
    else:
        return 0 # return lose

def guessing(word, words):
    # lists in which all the boards will be stored and all the guesses
    allBoards = []
    allGuesses = []
    wrongLetters= []
    # the player has six tries to guess the word
    for i in range(6):
        # the currBoard has 5 positions, of which all can be either a 0 - no match, a 1 - the letter is in the word or a 2 - the letter is on the exact this place
        currBoard = [0,0,0,0,0]
        ex = 0
        # inputting the guess
        guess = input("\n" + "-"*10 + f"\nGuess {i + 1}. word: ")
        # checking if the word exists:
        if guess in words:
            ex = 1
        # looping until the word inputted exists:
        while(ex != 1):
            # looping until the word inputted has five letters:
            while (len(guess) != 5 ):
                os.system("clear")
                print(f"The word {guess} is wrong length")
                print("-" * 10 + "\n")
                printBoards(allBoards, allGuesses, wrongLetters)
                print("\n")
                guess = input(f"Guess {i + 1}. word: ")
            # checking if exists:
            if guess in words:
                ex = 1
            else:
                os.system("clear")
                print(f"The word {guess} is not on the list")
                print("-" * 10 + "\n")
                printBoards(allBoards, allGuesses, wrongLetters)
                print("\n")
                guess = input(f"Guess {i + 1}. word: ")
        # appending the current guess to the list of all guesses
        allGuesses.append(guess)
        # checking all the letters in the guess with the drawn word:
        lettersThatAreInTheWord = []
        for position in range(5):
            # if the letter is in the word then the tile is 1, as mentioned before
            # we check if the letter appears in the word
            if (guess[position] in word):
                # now we check if we haven't already ack'd this letter
                if guess[position] not in lettersThatAreInTheWord:
                    # if so then we do add it to the board
                    currBoard[position] = 1
                    lettersThatAreInTheWord.append(guess[position])
            # if the letter is in the exact place in the word then the tile is 2
            if word[position] == guess[position]:
                currBoard[position] = 2
                # we check if the letter repeats
                if word[position] in word:
                    # if so we find its' 
                    ind = word.index(word[position])
                    if ind != position:
                        # if the letter was already mentioned that it does appear in tht word and we have found its' ecact location, we can then change the first appeareance of the letter (1 or yellow) to be neutral (0) as we don't want to repeat ourselves
                        if currBoard[ind] == 1:
                            currBoard[ind] = 0
            # if the guessed letter is not in the word and has not yet made its' way on the list of wrong letters then we add it there
            if (guess[position] not in word) and (guess[position] not in wrongLetters):
                    wrongLetters.append(guess[position])
        
        # appending the current board to the list of all boards
        allBoards.append(currBoard)
        # print all the boards along with the guesses
        os.system("clear")
        print("Right!\n" + "-" * 10 + "\n")
        printBoards(allBoards, allGuesses, wrongLetters)
        # check if the game has been won; if so return how many guesses it took
        if checkIfWon(currBoard) == 1:
            return len(allGuesses)
    # if the player exhausted all of their 6 guesses then the game is lost
    return 0