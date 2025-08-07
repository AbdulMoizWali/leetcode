"""
345. Reverse Vowels of a String
Easy
Topics
premium lock icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"



Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

from copy import deepcopy


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        I e  eA
        0 2  56

        list=[I,e,e,A]
        revered_list=[A,e,e,I]
        
        """
        s = s
        location_dic = {}
        vowels = ["a", "e", "i", "o", "u"]

        for i, val in enumerate(s):
            if str(val).lower() in vowels:
                location_dic[i] = val

        vowelList = list(location_dic.values())
        reversedList = []
        rev_counter = len(vowelList) - 1
        for val in vowelList:
            reversedList.append(vowelList[rev_counter])
            rev_counter -= 1
        counter = 0
        for index in location_dic:
            s = s[:index] + reversedList[counter] + s[index + 1 :]
            counter += 1
        # print(s)
        return s


sol = Solution()
print(sol.reverseVowels("IceCreAm") == "AceCreIm")
print(sol.reverseVowels("leetcode") == "leotcede")
print(sol.reverseVowels("race a car") == "raca e car")
print(sol.reverseVowels("race a car") == "raca e car")
print(sol.reverseVowels("aA") == "Aa")
print(sol.reverseVowels("hello") == "holle")
print(
    sol.reverseVowels("Yo! Bottoms up, U.S. Motto, boy!")
    == "Yo! Bottoms Up, u.S. Motto, boy!"
)
