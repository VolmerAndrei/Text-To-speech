import random
import requests
import csv
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
x=0
hiddenWord=[]
while x<len(word):
        hiddenWord.append("_ ")
        x=x+1
#hiddenWord=list(word)
check=""
while(True):
    letter=0
    if check==word:
        win=1
    check=""
    print(HANGMAN_STEPS[tryes])
    for _ in range(len(hiddenWord)):
        print(hiddenWord[_], end="")
    print("\n")
    if tryes==6 or win==1:
        break
    print ("\n")
    print("What character do you chose?")
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
        
    for _ in range(len(word)):
        check=check+hiddenWord[_]
    #print("Check is", check)
    
if win==1:
    print("*** Good Job!!!  You win!!! ***")
else:
    print("The word was **", word, "**")
    print("You lose!!! :(")
input('Press ENTER to exit')
    
        
     
    

