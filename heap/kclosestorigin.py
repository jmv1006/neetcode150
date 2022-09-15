import heapq

def kClosest(points, k):

    for point in points:
        distance = (point[0]**2) + (point[1]**2)
        point.insert(0, distance)
    
    heapq.heapify(points)

    result = []
    while len(result) < k:
        point = heapq.heappop(points)
        result.append([point[1], point[2]])
    
    return result
    
        


points = [[0,1], [1,0]]
print(kClosest(points, 2))