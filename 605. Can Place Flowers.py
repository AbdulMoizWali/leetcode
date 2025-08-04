"""
605. Can Place Flowers
Easy
Topics
premium lock icon
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from copy import deepcopy


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed_copy = deepcopy(flowerbed)
        flowers_len = len(flowerbed)
        for i, current in enumerate(flowerbed_copy):
            prev = flowerbed[i - 1] if i > 0 else 0
            next = flowerbed[i + 1] if i < flowers_len - 1 else 0
            if prev == 0 and current == 0 and next == 0:
                flowerbed[i] = 1
                n = n - 1 if n > 0 else 0
                if n == 0:
                    break
        return n == 0


"""
    We will be looping around the flowerbed deep copy array and we will first check if in the left there is nothing and in the next position if it is 0 then add 1 to the index
    000000000
    i=0
        prev = flowerbed[i-1] if i > 0 else 0
        current = flowerbed[i]
        next = flowerbed[i+1] if i < len(flowerbed) - 1 else 0
        if prev == 0 and current == 0 and next == 0
            flowerbed[i] = 1
            n--
    
    return n == 0
    
    
    

"""

sol = Solution()
# print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
# print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=1))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=2))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=3))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=4))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=5))
print(sol.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=6))
print(sol.canPlaceFlowers(flowerbed=[1, 1, 1, 1, 1], n=1))
print(sol.canPlaceFlowers(flowerbed=[0, 1, 1, 0, 0], n=1))
