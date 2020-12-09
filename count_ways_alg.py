def count_ways(n, m):
    s = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s[1][1] = 1
            s[i][j] = s[i - 1][j] + s[i][j - 1] + s[i - 1][j - 1]
    return s[n][m]

# magic numbers, names
