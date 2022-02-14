for testcases in range(int(input())):                                      

   friends_count, remove_count = list(map(int, input().split()))               

   friends =list(map(int, input().split()))                                 

   stack = []                                                                  

   for friend in friends:                                                      

       while remove_count and stack and stack[-1] < friend:                      

           stack.pop()                                                          

           remove_count -= 1                                                  

       stack.append(friend)                                                    

   print (' '.join(list(map(str, stack))))
