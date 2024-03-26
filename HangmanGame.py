import random
import requests
import csv

def FunctionHiddenWord():
    try:
        response=requests.get('https://random-word-api.herokuapp.com/word')
        words=response.json()
        word=random.choice(words)
    except requests.exceptions.ConnectionError as err:
        print("Connection Error")
        path=r'F:\Teme Programare\HangmanGame\Words.csv'
        with open(path, 'r') as f:
            reader=csv.reader(f)
            words=random.choice(list(reader))
            word = random.choice(words)
    return word

def FunctionEmptyWord(word):
    hiddenWord=[]
    x=0
    while x<len(word):
        hiddenWord.append("_ ")
        x=x+1
    return hiddenWord

def FunctionUserInput(letter, usedLetters, tryes):
    while letter==0:
        userInput=str(input())
        if len(userInput)==1:
            if userInput in word and userInput not in usedLetters:
                letter=1
                usedLetters.append(userInput)
                for y in range(len(word)):
                    if word[y]==userInput:
                        hiddenWord[y]=userInput    
            elif userInput in usedLetters:
                print("You already tried this one!")
            else:
                tryes=tryes+1
                usedLetters.append(userInput)
            break
        else:
            print("Please enter a single character!")  
    return usedLetters, tryes

def FunctionWinOrLose(win):
    if win==1:
        print("*** Good Job!!!  You win!!! ***")
    else:
        print("The word was **", word, "**")
        print("You lose!!! :(")
        
def FunctionPrintHangMan(tryes):
    print(HANGMAN_STEPS[tryes])
    for _ in range(len(hiddenWord)):
        print(hiddenWord[_], end="")
        
def FunctionCheck(check, word):
    if check==word:
        win=1
    else:
        win=0
    return win

HANGMAN_STEPS = [
"""
------
|  |
|
|
|
|
|
|___
""",
"""
------
|  |
|  O
|
|
|
|
|___
""",
"""
------
|  |
|  O
|  |
|
|
|
|___
""",
"""
------
|  |
|  O
| /|
|
|
|
|___
""",
"""
------
|  |
|  O
| /|\\
|
|
|
|___
""",
"""
------
|  |
|  O
| /|\\
| /
|
|
|___
""",
"""
------
|  |
|  O
| /|\\
| / \\
|
|
|___
"""
]

win=0
tryes=0
usedLetters=[]
#From a list
#words=["food", "cars", "home"]
#word=random.choice(words)

#From the internet
"""
try:
    response=requests.get('https://random-word-api.herokuapp.com/word')
    words=response.json()
    word=random.choice(words)
except requests.exceptions.ConnectionError as err:
    print("Connection Error")
    path=r'F:\Teme Programare\HangmanGame\Words.csv'
    with open(path, 'r') as f:
        reader=csv.reader(f)
        words=random.choice(list(reader))
        word = random.choice(words)
"""
word=FunctionHiddenWord()
"""
hiddenWord=[]
while x<len(word):
        hiddenWord.append("_ ")
        x=x+1
"""
hiddenWord=FunctionEmptyWord(word)
#hiddenWord=list(word)
check=""
while(True):
    letter=0
    """
    if check==word:
        win=1
    """
    win=FunctionCheck(check, word)
    check=""
    """
    print(HANGMAN_STEPS[tryes])
    for _ in range(len(hiddenWord)):
        print(hiddenWord[_], end="")
    """
    FunctionPrintHangMan(tryes)
    print("\n")
    if tryes==6 or win==1:
        break
    print ("\n")
    print("What character do you chose?")
    """
    while letter==0:
        userInput=str(input())
        if len(userInput)==1:
            if userInput in word and userInput not in usedLetters:
                letter=1
                usedLetters.append(userInput)
                for y in range(len(word)):
                    if word[y]==userInput:
                        hiddenWord[y]=userInput    
            elif userInput in usedLetters:
                print("You already tried this one!")
            else:
                tryes=tryes+1
                usedLetters.append(userInput)
            break
        else:
            print("Please enter a single character!")
    """   
    usedLetters, tryes=FunctionUserInput(letter, usedLetters, tryes)
    

    for _ in range(len(word)):
        check=check+hiddenWord[_]
    #print("Check is", check)

"""    
if win==1:
    print("*** Good Job!!!  You win!!! ***")
else:
    print("The word was **", word, "**")
    print("You lose!!! :(")
"""
FunctionWinOrLose(win)
input('Press ENTER to exit')
    
        
     
    

