# Write your code here
import random

guessword=['python','java','kotlin','javascript']

print('H A N G M A N')
rnd=random.choice(guessword)
wordlen=len(rnd)
hidden=['-']*wordlen
wordlist=[l for l in rnd]
count=8
allinputs=[]


while (True):
    choice=input('Type "play" to play the game, "exit" to quit: ')
    if choice=='play':
        while(count and '-' in hidden):
            print()
            print(''.join(hidden))
            letter=input('Input a letter: ')
            if len(letter)!=1:
                print('You should input a single letter')
                continue
            if not letter.islower():
                print('It is not an ASCII lowercase letter')
                continue
            index=[]
            if letter not in allinputs:
                allinputs.append(letter)
            else:
                print('You already typed this letter')
                continue

            if letter in wordlist:
                if letter in hidden:
                    print('You already typed this letter')
                    continue
                else:
                    index=[i for i, v in enumerate(wordlist) if v==letter]
            else:
                print('No such letter in the word')
                count-=1

            if index:
                for ind in index:
                    hidden[ind]=letter
        if '-' in hidden:
            print('You are hanged!')
            print()
        else:
            print()
            print(''.join(hidden))
            print("You guessed the word!")
            print("You survived!")
            print()
    elif choice=='exit':
        break
    else:
        pass

