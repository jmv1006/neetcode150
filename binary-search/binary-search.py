nums = [-1,0,3,5,9,12]
target = 1


def search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = round(len(nums) / 2)

    while(left <= right):
        if nums[mid] == target: return mid

        elif nums[mid] > target:
            right = mid - 1
            mid = round((left + right)/2)
        else:
            left = mid + 1
            mid = round((left + right)/2)

    return -1

search(nums, target)