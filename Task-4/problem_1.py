nums = list(map(int, input().split()))

mini = len(nums) - 1
inn= len(nums) - 1

for i in range(len(nums)):
	for j in range(i + 1, inn + 1):
	    if nums[i] == nums[j]:
    		mini=j-i
    		inn=j
    		break;

print(mini)
