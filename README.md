# Programming-Assignment-3-Highest-Value-Longest-Common-Sequence
Olivia Farino: 91264400

Boglarka Csanadi: 51900580

<h2>How to Run</h2>

python3 src/main.py<br> 
or<br>
python src/main.py

<h3>Output</h3>
Output is displayed in tests/example.out<br>
Output is also printed to the console

<h2>Questions</h2>
<h3>Question 1: Empirical Comparison</h3>

<h3>Question 2: Recurrence Equation</h3>

<h3>Question 3: Big-Oh</h3>

<h4>Psuedocode</h4>

    def HVLCS(A, B, values):
        for i=1 to len(A):
            for i=1 to len(B):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + values[A[i-1]])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(A)][len(B)]
                  
<h4>Runtime</h4>
O(m*n)<br>
m = length of A<br>
n = length of B
