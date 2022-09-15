import heapq

nums = [3,2,1,5,6,4]
k = 2

def findKthLargest(nums, k):
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)
    
    return nums[0]

findKthLargest(nums, k)