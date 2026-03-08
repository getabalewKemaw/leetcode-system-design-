class Solution(object):
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n):
        # ase cases
        if n == 1: return 1
        if n == 2: return 2
        
        # check if result is already in memo to fix the time limit execeded
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
