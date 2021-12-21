lst = list(map(int,input().strip().split()))

def Search(lst ,low,high,entry):
    for i in range(low,high):
        if entry == lst[i] :
            return int(i)
    else :
        return -1
    
        
    
    
    
   
        


pos = 0




count = list(map(lambda x : lst.count(x),lst))
l = len(lst)
mini = l+1
for i in range(l):
    m = 0 
    if count[i] > 1 :
        pos= Search(lst, i+1, l, lst[i])
        if pos >0:
            m = pos -i
            
            if(m <mini):
                mini = m
print(mini)
        
        
        
        