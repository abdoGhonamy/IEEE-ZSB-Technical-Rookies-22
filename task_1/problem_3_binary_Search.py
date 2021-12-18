def binary_Search(lst,entry):
    high = len(lst)-1
    low = 0
    mid = int((high+low)/2)
    
    while high >low:
        
        if lst[mid]==entry :
            return mid 
    
        elif lst[mid]<entry:
            low = mid+1 
            mid = int((high+low)/2)
        else :
            high = mid-1
            mid = int((high+low)/2)
    
    return -1


lst= [1,2,3,5,6,8,10,100,100,200,701]


print(binary_Search(lst,200))
