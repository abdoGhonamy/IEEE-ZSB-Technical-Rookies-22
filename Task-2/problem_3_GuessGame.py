from random import randint 

def search(char ,number):
    for i in range(3) :
        if char == number[i] :
            return i
    return -1

    
    
print("Enter a 3-digit number:")

randd = str(randint(100,1000))
guess = input()

while randd!=guess:
    hits = 0 
    exists = 0 
    for i in guess :
        pos = search(i,randd)
        if pos >= 0 :
            exists +=1
            if guess[pos]==randd[pos] :
                hits +=1
    print(hits," hit ",exists-hits," misses")    
    guess = input()
print("3 hit 0 misses")
    
        






