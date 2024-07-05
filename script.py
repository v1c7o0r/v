def solution(A):
    n = len(A)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    A.sort()
    
    for i in range(n):
        max_room_size = A[i]
        for j in range(i + 1, n + 1):
            if j - i <= max_room_size:
                dp[j] = min(dp[j], dp[i] + 1)
    
    return dp[n]

# Test cases
print(solution([1, 1, 1, 1, 1]))  # Output: 5
print(solution([2, 1, 4]))        # Output: 2
print(solution([2, 7, 9, 8]))     # Output: 2
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))  # Output: 4