#A. LISTS

#1
Islands= ['Trinidad', 'Jamaica', 'Barbados', 'Bermuda']
print (Islands)

#2
print (Islands[2])

#3
print([Islands[0:2]])

#4
L= ['Last']
Combine= Islands+L
print(Combine)

#5
print(len(Combine))
print ("List 1's Length:", len(Combine))

#6
del Combine[4]
print(Combine)
NewTry= ['New']
Combine_2= Combine+NewTry
print(Combine_2)



#B. STRINGS

#1
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
print(sentence_words)
print(" ".join(sentence_words))

#2
sentence_words.reverse()
print(sentence_words)

#3
sentence_words.sort()
print(sentence_words)

#4
print(sorted(sentence_words, key=len))



#C. RANDOM FUNCTION

#1
from random import randint
# this returns random integer: 100 <= number <= 1000
randnum = randint(1, 26)
print(randnum)
#Assertions
assert(0 <= randnum <= 26)
#assert(0 <= 45 <= 26),"You asserted something False (This was intentional as a test)"



#D. STRING FORMATTING FUNCTION


Truth= 'The number 1 bestseller today is: Lemonade by Beyonce'
print(Truth)
#'The number 1 bestseller today is: Lemonade by Beyonce'.title
print('The number 1 bestseller today is: Lemonade by Beyonce'.title())
print('The number {0} bestseller today is: {1} Pilots'.format(2,21))



#E. PASSWORD VALIDATION FUNCTION

CAPS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
sym = ('!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=')
numba = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

print(CAPS)
word = input("Please Enter a Valid Password. Password must contain at least 2 digits, at least one capital letter, must be at least 8 to 14 characters long and contain one of the following:'!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=':    ")

def capitale(word2):
    global CAPS, sym, numba
    caps_counter = 0
    sym_counter = 0
    num_counter = 0
    for i in word2:
        if i in CAPS:
            caps_counter += 1
        elif i in sym:
            sym_counter += 1
        elif i in numba:
            num_counter += 1
    if (caps_counter >= 1 and sym_counter >= 1 and len(word2) >= 8 and len(word2) <= 14 and num_counter >= 2):
        print('Valid Password. Success! :-)')
    else:
        print('Password is invalid. Please see the above instructions.')
capitale(word)


#Exp Problem
base = int(input("Enter Base:  "))
power = int(input("Enter Power:  "))

def exp(numb, multi):
    if multi == 0:
        if numb == 0: 
            print("0 to the power of 0 is undefined")
        else:
            print(1)
    else: 
        temp = numb
        for i in range(multi - 1):
            temp = temp*numb
            print(temp)
exp(base,power)    
