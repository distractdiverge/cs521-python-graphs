import numpy as np


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    b = np.full((m, n), -1, dtype=np.int32)
    c = np.full((m, n), -1, dtype=np.int32)

