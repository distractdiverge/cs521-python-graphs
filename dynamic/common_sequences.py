

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    print("m={0}; n={1}".format(m,n))

    # Create 2-d arrays
    b = [[-1 for j in range(1, m)] for i in range(1, n)]
    c = [[-1 for j in range(0, m)] for i in range(0, n)]

    for i in range(1, m):
        c[i][0] = 0

    for j in range(0, n):
        c[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[i]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'top-left' # TODO: Find the cell to the top-left
            elif c[i - 1][j] >= c[i, j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 'up' # TODO Find the cell above
            else:
                c[i][j] = c[i, j - 1]
                b[i][j] = 'left' # TODO find cell to left

    return b, c



