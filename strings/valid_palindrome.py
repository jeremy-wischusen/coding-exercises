'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution:
    def solve(self, s: str) -> bool:
        an = ''.join(c for c in s if c.isalnum()).lower()
        return an[::-1] == an


'''
pytest
'''
solution = Solution()


def test_is_palindrome():
    assert solution.solve('A man, a plan, a canal: Panama') == True


def test_is_not_palindrome():
    assert solution.solve('race a car') == False
