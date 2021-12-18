def summm(n):
    return int(n*(n+1)/2)



n = int(input())


first = int(n/3)
second = int(n/5)
eror = int(n/15)


summ = ((3*(summm(first)))+(5*summm(second)))-(summm(eror)*15)

print(summ)


