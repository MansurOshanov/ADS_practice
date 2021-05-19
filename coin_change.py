class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        BFS approach can work, but it takes too much ime to check each combination
        '''
#         memo = {}
#         def bfs():
#             queue = collections.deque()
#             queue.append(amount)

#             depth = 1

#             if amount == 0:
#                 return 0

#             while queue:
#                 size = len(queue)
#                 for i in range(size):
#                     n = queue.popleft()
#                     for coin in coins:
#                         if n - coin == 0:
#                             return depth
#                         queue.append(n-coin)
#                 depth += 1
#             return -1
                    
        dp = [float("inf") for i in range(0, amount + 1)]
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(dp[a], dp[a-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1