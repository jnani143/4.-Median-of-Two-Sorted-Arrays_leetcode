class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marge=nums1+nums2
        marge.sort()
        n=len(marge)
        if n%2!=0:
            return marge[(n-1)//2]
        else:
            return (marge[(n//2)-1]+marge[n//2])/2
