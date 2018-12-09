from dynamic.common_sequences import lcs_length


def main_lcs():
    print_lcs("a", "a")
    print_lcs("ab", "ab")
    print_lcs("abc", "abc")
    print_lcs("a", "ab")
    print_lcs("ab", "a")
    print_lcs("ba", "a")
    print_lcs("a", "ba")


def print_lcs(x, y):
    length = lcs_length(x, y)

    print("Longest Common Sequence of: {0} and {1}".format(x, y))
    print("Length: {0}".format(length))
    print("\n")
    return length


if __name__ == "__main__":
    main_lcs()
