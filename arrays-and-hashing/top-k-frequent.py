nums = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
k = 4


def topKFrequent(nums, k):
    ##create a hashmap that contains the amount of occurences for each value in nums
    frequencies = {}

    for num in nums: ##O(n)
        if(num in frequencies):
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    
    res = []

    for num in range(1, k + 1): ##O(k)
        max_key = max(frequencies, key=frequencies.get)
        res.append(max_key)
        frequencies.pop(max_key, None)
    
    print(res)

    ##O(n + k)



        


topKFrequent(nums, k)



        