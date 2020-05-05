''' 
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters. 
'''


from collections import defaultdict


class Solution:
    def solve(self, s: str):
        ht = defaultdict(int)
        for i in s:
            ht[i] += 1

        for i, c in enumerate(s):
            if ht[c] == 1:
                return i
        return -1


''' pytest '''
solution = Solution()


def test_case_1():
    assert solution.solve("leetcode") == 0  # the l


def test_case_2():
    assert solution.solve("loveleetcode") == 2  # the v


def test_case_3():
    assert solution.solve("") == -1  # the v
