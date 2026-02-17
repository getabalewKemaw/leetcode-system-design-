class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        operations = []
        target_set = set(target) # For faster lookup
        last_needed = target[-1] # The point where we stop
        
        current_target_index = 0
        for i in range(1, n + 1):
            # Rule 3: Stop if the stack equals target
            if current_target_index == len(target):
                break
                
            # Every number from the stream is Pushed initially
            operations.append("Push")
            
            # Check if the current stream number is the one we need
            if i == target[current_target_index]:
                # It matches! Keep it and move to the next target element
                current_target_index += 1
            else:
                # It doesn't match! Pop it immediately
                operations.append("Pop")
                
        return operations

            