import random
import string
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