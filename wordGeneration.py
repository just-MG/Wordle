import random
# converting this huge lists into python list
with open("wordlist.txt") as f:
    words = f.readline().split(",")
# a function which returns the list
def listOfWords():
    return words
# a function which generates a random word
def generateWord():
    return words[random.randint(0,len(words) - 1)]
