from collections import Counter

 

for _ in range(int(input())):

   s, t = Counter(input()), Counter(input())

   count = 0

 

   for k, v in t.items():

       if k in s:

           count += abs(s[k] - v)

       else:

           count += v

   for k, v in s.items():

       if k not in t:

           count += v

 

   print(count)
