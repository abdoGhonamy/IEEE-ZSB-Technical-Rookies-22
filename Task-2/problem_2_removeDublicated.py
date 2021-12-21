lst = (input().strip().split())
def print_t(s):
    print(s,end=" ")
#list(map(print_t,sorted(lst))) O(nlog(n)+n)--> slow
l = len(lst)
s = lst[0]
print(s,end=" ")
for i in range(l) :#O(n)
    
    
    if(lst[i]!=s):
        print_t(lst[i])
    s = lst[i]

            