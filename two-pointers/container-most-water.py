def maxArea(height):
    p1 = 0
    p2 = len(height) - 1

    areas = {}

    while(p1 < p2):
        width = p2 - p1
        length = min(height[p1], height[p2])
        area = width * length
        
        areas[area] = area

        if(height[p1] > height[p2]):
            p2 -= 1
        else:
            p1 += 1

    return max(areas)

h = [1,1]
print(maxArea(h))