def Selection_Sort(lst,l):
    for i in range(l):
        mini = i 
        for y in range(i,l):
            if lst[mini] >lst[y]:
                mini = y 
        lst[mini],lst[i]=lst[i],lst[mini]
        


lst = [1 ,4, 5, 2, 1 ,4]

l = len(lst)

Selection_Sort(lst, l)


print(lst)


