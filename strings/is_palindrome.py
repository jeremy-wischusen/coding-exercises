def is_palindrome(s):
    r = s[::-1]

    if r == s:
        return True

    return False


'''
pytest
'''


def test_is():
    assert is_palindrome('racecar') == True


def test_is_not():
    assert is_palindrome('motorcycle') == False
