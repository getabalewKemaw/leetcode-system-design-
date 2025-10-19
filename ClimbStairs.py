class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
sol=Solution()
print(sol.climbStairs(5))

# lets make it faster by using dynamic programming


class Solution1(object):
    def climbStairs(self, n):
        # if only 1 or 2 steps, just return n
        if n <= 2:
            return n
        
        # start from step 1 and 2
        one_step_before = 2  # ways to reach (n-1)
        two_steps_before = 1 # ways to reach (n-2)

        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before

sol1=Solution1()
print(sol1.climbStairs(5))