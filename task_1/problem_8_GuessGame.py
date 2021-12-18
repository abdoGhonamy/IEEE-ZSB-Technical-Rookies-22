from random import randint


guess = int(input())
randd = randint(1,10)
trie = 1 
while guess !=randd:
    print("Wrong guess")
    guess = int(input())
    trie +=1 
print("Yay you got it ",trie," tries")

    
