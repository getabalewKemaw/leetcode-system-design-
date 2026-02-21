class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # three  pointers:
        p1 = m - 1      
        p2 = n - 1      
        p = m + n - 1   

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are leftovers in nums2, copy them
        # (We don't need to check p1 because they are already in nums1)
        nums1[:p2 + 1] = nums2[:p2 + 1]
