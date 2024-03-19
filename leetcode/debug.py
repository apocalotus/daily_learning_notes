def solution(heights, bricks, ladders):
    min_c = 0
    if ladders > 0:
        max_climbs = [0] * ladders
    else:
        min_c = inf
    for i in range(len(heights)-1):
        
        
        if heights[i+1] - heights[i] > min_c:
            max_climbs[0] = heights[i+1] - heights[i]
            bricks -= min_c
            min_c = min(max_climbs)
            max_climbs.sort(reverse=False)
        elif heights[i+1] - heights[i] > 0:
            bricks -= heights[i+1] - heights[i]
        
            
        if bricks < 0:
            return i
    
    return len(heights)-1

solution([4,12,2,7,3,18,20,3,19], 10, 2)