#   these is two filnd the median of two sorted arrays
def findMedianSortedArrays(nums1, nums2):
    # merge the two sorted arrays
    merged=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

    while i<len(nums1):
        merged.append(nums1[i])
        i+=1
    while j<len(nums2):
        merged.append(nums2[j])
        j+=1
    n=len(merged)
    # find the median
    if n%2==1:
        return merged[n//2]
    else:
        return (merged[n//2 - 1] + merged[n//2]) / 2.0
# Example usage:
nums1 = [1, 3]
nums2 = [2,5]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0ef findMedianSortedArrays(nums1, nums2):
    # merge the two sorted arrays
