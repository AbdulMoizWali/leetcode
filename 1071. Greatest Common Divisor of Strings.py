"""
1071. Greatest Common Divisor of Strings
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        """
        str1 = ABABAB
        str2 = ABAB
        
        smallest = ABAB
        x = A
        
        check till the length of the words
        (len(ABABAB)//len(A)) = A * (6//1)
        A + A + A + A + A + A != ABABAB 
        A + A + A + A != ABAB
        
        
        Then add one more letter to x
        x = AB
        check till the length of the words
        AB + AB == ABAB
        """
        len1 = len(str1)
        len2 = len(str2)

        len_smallest = min(len1, len2)
        smallest = str1 if len(str1) == len_smallest else str2

        highest_gcd = ""
        x = ""
        len_x = 0

        multiplier1 = 1
        multiplier2 = 1

        for i in range(0, len_smallest):
            x += smallest[i]
            len_x = len(x)
            if (len1 % len_x != 0) and (len2 % len_x != 0):
                continue
            multiplier1 = len1 // len_x
            multiplier2 = len2 // len_x

            multiplied1 = x * multiplier1
            multiplied2 = x * multiplier2

            # print(f"x: {x}")
            # print(f"multiplier1: {multiplier1}")
            # print(f"multiplier2: {multiplier2}")
            # print(f"multiplied1: {multiplied1}")
            # print(f"multiplied2: {multiplied2}")

            if (multiplied1 == str1) and (multiplied2 == str2):
                highest_gcd = x
                continue
        return highest_gcd


sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("ABABABAB", "ABAB"))
print(sol.gcdOfStrings("LEET", "CODE"))
print(sol.gcdOfStrings("ABCABCD", "ABC"))
print(sol.gcdOfStrings("ABCABC", "A"))
print(sol.gcdOfStrings("ABCABC", ""))
print(
    sol.gcdOfStrings(
        "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    )
)
