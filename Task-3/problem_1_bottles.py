numberOfButtles = int(input())
spaces=list()
water = 0

for i in range(numberOfButtles):
    remain,capacity = input().strip().split()
    spaces.append(int(capacity)-int(remain))
    water += int(remain)


if(water<=(spaces[-1]+spaces[-2])):
    print("Yes")
else :
    print("No")
    
