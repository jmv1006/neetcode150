
def twoSum(nums, target):
    sums = {}

    for x in range(len(nums)):
        diff = target - nums[x]
        if(diff in sums):
            return [sums[diff] + 1, x + 1]
        else:
            sums[nums[x]] = x

numbers = [-1, 0]
target = -1

print(twoSum(numbers, target))