from dynamic.common_sequences import lcs_length


def main_lcs():
    X = "abc123"
    Y = "abc1234"

    b, c = lcs_length(X, Y)

    print("Longest Common Sequence of: {0} and {1}".format(X, Y))

    for row in b:
        print(row)

    print("\n")

    for row in c:
        print(row)


if __name__ == "__main__":
    main_lcs()
