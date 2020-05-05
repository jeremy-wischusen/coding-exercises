"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
Solution from https://medium.com/@d_dchris/10-methods-to-solve-the-longest-common-prefix-problem-using-python-leetcode-14-a87bb3eb0f3a
"""


class Solution:
    def solve(self, strs: list):
        longest = ""
        if not strs:
            return longest
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            if all([x.startswith(shortest[:i+1]) for x in strs]):
                longest = shortest[:i+1]
            else:
                break

        return longest


''' pytest '''
solution = Solution()


def test_case_1():
    assert solution.solve(["flower", "flow", "flight"]) == "fl"


def test_case_2():
    assert solution.solve(["dog", "racecar", "car"]) == ""


def test_case_3():
    assert solution.solve(["a"]) == "a"


def test_case_4():
    assert solution.solve([]) == ""


def test_case_5():
    assert solution.solve([""]) == ""


def test_case_6():
    assert solution.solve(["", ""]) == ""


def test_case_7():
    assert solution.solve(["", "flow"]) == ""


def test_case_8():
    assert solution.solve(["flow", ""]) == ""


def test_case_10():
    assert solution.solve(["a", "a", "b"]) == ""
