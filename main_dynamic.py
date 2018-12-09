import random
from dynamic.common_sequences import lcs_length, inc_sequence


def main_lcs():
    print_lcs("a", "a")
    print_lcs("ab", "ab")
    print_lcs("abc", "abc")
    print_lcs("a", "ab")
    print_lcs("ab", "a")
    print_lcs("ba", "a")
    print_lcs("a", "ba")

    print_lcs([1], [1])
    print_lcs([1], [1, 2])

    print("Length of Monotonically Increasing sequence: {0}".format(inc_sequence([2, 3, 4, 4, 2])))
    print("Length of Monotonically Increasing sequence: {0}".format(inc_sequence([1, 1, 4, 4, 2])))
    print("Length of Monotonically Increasing sequence: {0}".format(inc_sequence([2, 2, 4, 4, 2])))
    print("Length of Monotonically Increasing sequence: {0}".format(inc_sequence([2, 3, 5, 4, 2])))
    print("Length of Monotonically Increasing sequence: {0}".format(inc_sequence([0, 2, 4, 4, 2])))

    test_inc()
    test_inc()
    test_inc()
    test_inc()


def print_lcs(x, y):
    length = lcs_length(x, y)

    print("Longest Common Sequence of: {0} and {1}".format(x, y))
    print("Length: {0}".format(length))
    print("\n")
    return length


def test_inc():
    print("\n")
    x = [random.randint(0, 10) for i in range(0, 10)]

    print("Input: {0}".format(x))

    lengths, max_length = inc_sequence(x)

    print("Result: {0}; Max Length: {1}".format(lengths, max_length))


if __name__ == "__main__":
    main_lcs()
