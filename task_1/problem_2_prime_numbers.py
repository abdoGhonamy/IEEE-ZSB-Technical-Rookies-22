def prime(num):
    if num == 2 :
        return 1;
    if num%2==0 and num !=2:
        return 0;
    for i in range(3,num,2):
        if num % i==0 and num!=i :
            return 0 ;
    return 1 ;

num = int(input())

for i in range(2,num+1):
    if prime(i)==1:
        print(i,end=" ")

            