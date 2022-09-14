
from operator import neg


def longestConsecutive(nums):
    if len(nums) < 1: return 0
    numSet = set(nums)
    longest = 0
    lengths = {}
    for num in nums:
        ##check if start of sequence
        if(num - 1 not in numSet):
            length = 1
            while(num + 1 in numSet):
                length += 1
                num = num + 1
            lengths[length] = length
    
    print(max(lengths))


        




#nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [100,4,200,1,3,2]
#nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# nums = [0, -1]
longestConsecutive(nums)