def solution(n):
    ways = [[0 for i in range(n + 1)] for j in range(n + 1)]
    ways[0][0] = 1 
    
    for last in range(1, n + 1):
        for leftSet in range(0, n + 1):
            print(leftSet)
            ways[last][leftSet] = ways[last - 1][leftSet]
            if leftSet >= last:
                ways[last][leftSet] += ways[last - 1][leftSet - last]
    
    return ways[n][n] - 1

print(solution(200))
