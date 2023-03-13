# ECOR 1042 Lab 1

__author__ = "Samuel Burt"
__student_number__ = "101260404"

# ======================================================
# Exercise 1


def replicate(prompt: str) -> str:
    """Copies a prompt a number of times, depending on the length of said prompt.

    Examples:
    >>> replicate('str')
    'strstrstr'
    >>> replicate('s')
    's'
    >>> replicate('star')
    'starstarstarstar'
    """
    return prompt * len(prompt)

# ======================================================
# Exercise 2


def repeat_separator(word: str, sep: str, n: int) -> str:
    """Returns string containing int variable n occurences of variable word, seperated by the string variable sep.

    Preconditions: len(word) * len(sep) > 0, n >= 0

    Examples:
    >>> repeat_separator("Word", "X", 3)
    "WordXWordXWord"
    >>> repeat_separator("This", "And", 2)
    "ThisAndThis"
    >>> repeat_separator("This", "And", 1)
    "This"
    """
    final_word = word
    for i in range(n - 1):
        final_word += sep + word
    return final_word

# ======================================================
# Exercise 3


def has_pair(s: str, ch: str) -> bool:
    """Returns boolean value depending on if string variable s contains at least two consecutive occurences of string variable ch.

    Preconditions: len(s) > 1, len(ch) == 1

    Examples:
    >>> has_pair('abccd', 'c')
    True
    >>> has_pair('abcdc', 'c')
    False
    >>> has_pair('abbcd', 'c')
    False
    """
    for i in range(len(s) - 1):
        if s[i] == ch and s[i + 1] == ch:
            return True
    return False

# ======================================================
# Exercise 4


def middle_way(nums_a: list, nums_b: list) -> list:
    """Returns a new list containing the element at the middle of b list and a list.

    Preconditions: len(nums_a) == len(nums_b) == 3

    Examples:
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([1, 6, 3], [4, 4, 6])
    [6, 4]
    >>> middle_way([1, 4, 3], [4, 2, 6])
    [4, 2]
    """
    del nums_a[0], nums_a[-1], nums_b[0], nums_b[-1]
    return nums_a + nums_b

# ======================================================
# Exercise 5


def make_ends(integer_lst: list) -> list:
    """Returns a new list with the first and last element of given lst_int list.

    Preconditions: len(integer_lst) > 0

    Examples:
    >>> make_ends([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 10]
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([4, 5, 6, 7])
    [4, 7]
    """
    return [integer_lst[0], integer_lst[-1]]

# ======================================================
# Exercise 6


def common_end(nums_a: list, nums_b: list) -> bool:
    """Returns boolean value depending on wether or not the first or last characters of both lists match.

    Preconditions: len(nums_a) > 0, len(nums_b) > 0

    Examples:
    >>> common_end([0, 1, 2], [1, 2, 3])
    False
    >>> common_end([1, 1, 2], [1, 2, 3])
    True
    >>> common_end([0, 1, 3], [1, 2, 3])
    True
    """
    return nums_a[0] == nums_b[0] or nums_a[-1] == nums_b[-1]

# ======================================================
# Exercise 7


def count_evens(integer_lst: list) -> int:
    """Returns the number of even numbers in a given list.

    Examples:
    >>> count_evens([0, 1, 2, 3, 4, 5, 6, 7])
    4
    >>> count_evens([1, 3, 5, 7])
    0
    >>> count_evens([])
    0
    """
    count = 0
    for i in range(len(integer_lst)):
        if integer_lst[i] % 2 == 0:
            count += 1
    return count

# ======================================================
# Exercise 8


def big_diff(nums: list) -> int:
    """

    Preconditions: len(nums) >= 2

    Examples:
    >>>
    >>>
    >>>
    """
    pass

# ======================================================
# Exercise 9


def has22(nums: list) -> bool:
    """Returns boolean value depending on wether or not there are at least two 2's next to each other in list nums.

    Examples:
    >>> has22([1, 2, 2, 3])
    True
    >>> has22([4, 2, 3, 2])
    False
    >>> has22([])
    False
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


# ======================================================
# Exercise 10

def centered_average(nums: list) -> int:
    """Returns the centered average of a given list of integers.

    Preconditions: len(nums) >= 3

    Examples:
    >>>
    >>>
    >>>
    """
    pass
# ======================================================
# Exercise 11


def bank_statement(bank_history: list) -> list:
    """Returns the sum of deposits, sum of withdrawals, and the total balance of a given bank history.

    Preconditions: len(bank_history) > 0

    Examples:
    >>> bank_statement([-100.3044, 200.2122, -399.62, 523.0])
    [723.21, -499.92, 223.29]
    >>> bank_statement([3.65, -3.65, 4.55, 2.45])
    [10.65, -3.65, 7.0] 
    >>> bank_statement([0.000, 10.5, -10.5])
    [10.5, -10.5, 0.0]
    """
    deposits = 0
    withdrawals = 0
    for transaction in bank_history:
        if transaction > 0:
            deposits += transaction
        else:
            withdrawals += transaction
    return [round(deposits, 2), round(withdrawals, 2), round(sum(bank_history), 2)]


# ======================================================
# Exercise 12


def reverse(nums: list) -> list:
    """Reverses a given list.

    Examples:
    >>> reverse([4, 2, 3, 2])
    [2, 3, 2, 4]
    >>> reverse([0, 1, 2, 3])
    [3, 2, 1, 0]
    >>> reverse([])
    []
    """
    new_list = []
    for i in range(len(nums)):
        new_list += [nums[(-i) - 1]]
    return new_list



