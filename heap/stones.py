import heapq
##x == y, destroy both
## x != y, y = y - x

def lastStoneWeight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        heapq.heapify(stones)
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if first != second:
            difference = first - second
            stones.append(difference)
    
    if stones: return abs(stones[0])
    else: return 0
    
            
    

        



stones = [9, 10, 1, 7, 3]
print(lastStoneWeight(stones))