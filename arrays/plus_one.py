#!/usr/bin/python
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Solution
Overview
"Plus One" is a subset of the problem set "Add Number", which shares the same solution pattern.

All these problems could be solved in linear time, and the question here is how to solve it without using the addition operation or how to solve it in constant space complexity.

The choice of algorithm should be based on the format of input. Here we list a few examples:

Integers

Usually the addition operation is not allowed for such a case. Use Bit Manipulation Approach. Here is an example: Add Binary.

Strings

Use bit by bit computation. Note, sometimes it might not be feasible to come up a solution with the constant space for languages with immutable strings, e.g. for Java and Python. Here is an example: Add Binary.

Linked Lists

Sentinel Head + Schoolbook Addition with Carry. Here is an example: Plus One Linked List.

Arrays (also the current problem)

Schoolbook addition with carry.

Note that, a straightforward idea to convert everything into integers and then apply the addition could be risky, especially for the implementation in Java, due to the potential integer overflow issue.

As one can imagine, once the array gets long, the result of conversion cannot fit into the data type of Integer, or Long, or even BigInteger.



Approach 1: Schoolbook Addition with Carry
Intuition

Let us identify the rightmost digit which is not equal to nine and increase that digit by one. All the following consecutive digits of nine should be set to zero.

Here is the simplest use case which works fine.

simple

Here is a slightly complicated case which still passes.

more

And here is the case which breaks everything, because all the digits are nines.

handle

In this case, we need to set all nines to zero and append 1 to the left side of the array.

append

Algorithm

Move along the input array starting from the end of array.

Set all the nines at the end of array to zero.

If we meet a not-nine digit, we would increase it by one. The job is done - return digits.

We're here because all the digits were equal to nine. Now they have all been set to zero. We then append the digit 1 in front of the other digits and return the result.

Implementation

Current
1 / 7

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1 
                digits[idx] += 1
                # and the job is done
                return digits
                
        # we're here because all the digits are nines
        return [1] + digits

Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) since it's not more than one pass along the input list.

Space complexity : \mathcal{O}(1)O(1) when digits contains at least one not-nine digit, and \mathcal{O}(N)O(N) otherwise.
Analysis written by @liaison and @andvary
'''


class Solution:
    def solve(self, digits: list) -> list:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits


'''
pytest
'''
solution = Solution()


def test_case_1():
    assert solution.solve([1, 2, 3]) == [1, 2, 4]


def test_case_2():
    assert solution.solve([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_case_3():
    assert solution.solve([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
