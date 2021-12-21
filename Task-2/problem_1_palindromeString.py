string = input().strip();

l = len(string)

mid = int(l/2)

x = 0
y = l-1


palindrome = True
for  i in range(mid):
    if(string[i]!=string[y]):
        palindrome = False ;
        break;
    
    y-=1
    
if(palindrome):
    print("yes")
else :
    print("no")
    
    