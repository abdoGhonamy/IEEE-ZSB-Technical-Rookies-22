sent = input().strip().split()
lenghs = list(map(len,sent))
ma = max(lenghs)
print("**"+ma*"*"+"**")
for i in range(len(sent)):
    print("* "+sent[i]+(ma-lenghs[i])*" "+" *")
print("**"+ma*"*"+"**")