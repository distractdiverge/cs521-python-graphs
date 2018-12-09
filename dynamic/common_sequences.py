def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    print("m={0}; n={1}".format(m, n))

    # Initialize 2-d arrays
    b = [[-1 for j in range(0, n+1)] for i in range(0, m+1)]
    c = [[-1 for j in range(0, n+1)] for i in range(0, m+1)]

    for i in range(0, m+1):
        c[i][0] = 0

    for j in range(0, n+1):
        c[0][j] = 0

    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i+1][j+1] = 'top-left' # TODO: Find the cell to the top-left
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i+1][j+1] = 'up' # TODO Find the cell above
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i+1][j+1] = 'left' # TODO find cell to left

    return c[m][n]



