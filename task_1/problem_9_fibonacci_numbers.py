def fibonacci_numbers(num):
    first = 0
    print(first,end = " ")
    second = 1
    
    new = first+second
    for i in range(num-1):
        print(new,end=" ")
        new = first+second
        first = second
        second =new 
        
num = int(input())        
        
fibonacci_numbers(num)