def unique_paths(m, n):
    def solve(i, j):
        if i == m-1 or j == n-1:
            return 1
        if dp[i][j] != 0:
            return dp[i][j]

        dp[i][j] = solve(i+1, j) + solve(i, j+1)
        return dp[i][j]

    dp = [[0 for i in range(n)] for j in range(m)]
    return solve(0, 0)

if __name__ == "__main__":
    paths = unique_paths(6, 3)
    print(f"Number of paths = {paths}.")