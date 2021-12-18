def sum_with_Recursion(lst):
    if len(lst)==1:
        lst[0]
        return lst[0]
    else :
        return lst[0]+sum_with_Recursion(lst[1:])
    
def sum_with_forLoop(lst):
    sum= 0 
    for i in lst :
        sum+=i
    return sum
def sum_with_whileLoop(lst):
    i = len(lst)-1
    sum = 0 
    while i>=0:
        sum +=lst[i]
        i-=1
    return sum



n = input()
lst =list( map(int,input().strip().split()))
print(sum_with_Recursion(lst))
print(sum_with_forLoop(lst))
print(sum_with_whileLoop(lst))
