import string 
from random import randint

lower = string.ascii_lowercase
upper = string.ascii_uppercase
char = ['@', '#', '$', '%', '&']
password = ''
i = randint(0, 25)
while len(password)<10:
    password += (lower[i]+upper[i]+str(i)+char[i%4])
    i=randint(0,25)
print(password)

    
    





