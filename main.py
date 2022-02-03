import wordGeneration as wd
import guessing as g
import os

def main():
    #setting the variables:
    plya = 1
    score = 0
    count = 0
    # looping so the player can play as many times as they want to
    while plya:
        os.system("clear")
        count += 1
        # Generating words using the other files
        word = wd.generateWord()
        words = wd.listOfWords()
        # v the whole guessing takes place here
        outcome = g.guessing(word, words)
        # checking for the score
        if outcome != 0:
            print("\n" + "-"*20)
            score += 1
            print(f"You've guessed it! The word was indeed {word}. It took you {outcome} guesses. ")
        else:
            print("\n" + "-"*20)
            print(f"Sorry:(. The word was {word}. Better luck next time")
        # formatting
        print("-"*20 + "\n")
        # checking whether the player wants to play again
        ans = input("Do you want to play again? [y / n]\n")
        if ans == 'y':
            pass
        elif ans == 'n':
            plya = 0
            print(f"Thanks for playing! Your score is {score} games won out of total {count}.\n")
        else:
            print("invalid input")
            print(f"Thanks for playing! Your score is {score} games won out of total {count}.\n")
            return
        

if __name__ == "__main__":
    main()