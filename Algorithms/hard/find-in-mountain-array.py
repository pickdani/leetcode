# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# O(3logn) = O(logn)
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        # find peak /\
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1): # peak on right
                l = m + 1
            else: # peak on left
                r = m
        peak = l

        # search 0 to peak, /
        l = 0
        r = peak
        while l < r:
            m = (l + r) // 2
            middle_val = mountain_arr.get(m);
            if target == middle_val:
                return m
            elif target > middle_val: # target on right
                l = m + 1
            else: # peak on left
                r = m

        # search peak to n, \
        l = peak
        r = n
        while l < r:
            m = (l + r) // 2
            middle_val = mountain_arr.get(m);
            if target == middle_val:
                return m
            elif target < middle_val: # target on right
                l = m + 1
            else: # peak on left
                r = m

        return -1