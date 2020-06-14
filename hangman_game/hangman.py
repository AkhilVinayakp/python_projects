
import random
import string
import argparse

'''

test code for random word generation 

alpha = string.ascii_lowercase          #ust using lowercase letters to create a random word
length = 6 # maximum length of the string set to 6

print(alpha[8])
#print(random.choice([i for i in range(0,10)]))
word = "".join([random.choice(alpha) for i in range(0,10)])
print(word)


wd=[]
for i in range(len(alpha)):
    if len(wd) >= 6:
        break
    else:
        s = random.choice(alpha)
        if s in wd:
            continue
        else:
            wd.append(s)
            

print("".join(wd))

'''


# the following code will return the word . 
# level is the length of the word we need to predict
# << update required >> the word should be in english dictionary , a proper english word
def get_rand_word(level):
    alpha = string.ascii_lowercase
    word = []
    for i in range(len(alpha)):
        if len(word) == level:
            break
        else:
            s =random.choice(alpha)
            if s in word:
                continue
            else:
                word.append(s)
    return "".join(word)


# main part of the hangman game

parser = argparse.ArgumentParser(description="hangman game to kill time")
parser.add_argument('-l','--level', default=6, help =" level of the game default is 6")

print("H A N G M A N!")
print("the game about to begin")

def main():
    args = parser.parse_args()
    word = get_rand_word(args.level)
    miss = 0
    found = 0
    correct = 0
    while miss!=8 and found != args.level:
        ch = input("> predict the charecter \n >")
        if ch in word:
            print("> WOW thats correct")
            found+=1
        else:
            miss+=1
            print("> Oh no that was a miss \t\t >life {}".format(8-miss))
    if found == args.level:
        print("<<<<<<<<<<<<<<<<<<<<victory>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else:
        print("<<<<<<<<<<<<<<<<<<<<<hanged!!!!!!!!!!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("the correct word is {}".format(word))



s = input("press y to continue")        
if s == 'y':
	main()
else:
	print("exiting")



















