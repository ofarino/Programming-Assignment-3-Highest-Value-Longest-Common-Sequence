def read_example_in(file_path):
    with open(file_path, 'r') as file:
        K = int(file.readline().strip())
        values = {}
        for _ in range(K):
            char, value = file.readline().strip().split()
            values[char] = int(value)

        A = file.readline().strip()
        B = file.readline().strip()
    return values, A, B

def highest_val_longest_common_sequence(str1, str2, values):    
    m = len(str1)
    n = len(str2)
    # 2d arr to store highest value of longest common sequence at each point
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + values.get(str1[i - 1], 0))
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # backtrack
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1] and dp[i][j] == dp[i - 1][j - 1] + values.get(str1[i - 1], 0):
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    return dp[m][n], ''.join(lcs)

if __name__ == "__main__":
    print("hi")