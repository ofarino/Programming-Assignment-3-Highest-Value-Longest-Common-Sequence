# Programming-Assignment-3-Highest-Value-Longest-Common-Sequence
Olivia Farino: 91264400

Boglarka Csanadi: 51900580

<h2>How to Run</h2>
<h3>Running Main</h3>
python3 src/main.py<br> 
or<br>
python src/main.py

<h3>Main Output</h3>
Output is displayed in tests/example.out<br>
Output is also printed to the console

<h3>Running Tests for Question1</h3>
python3 -m tests.empirical_comparison<br>
or<br>
python -m tests.empirical_comparison

<h3>Other Tests' Output</h3>
Output is displayed in tests/test.out


<h2>Questions</h2>
<h3>Question 1: Empirical Comparison</h3>

<h3>Question 2: Recurrence Equation</h3>

**Define OPT**: OPT(i, j) = length/max value of the longest common subsequence between the first i characters of A and the first j characters of B


**Base Case: One of the strings has length 0 (Both equations cover the case of both strings having length 0)**


• OPT(0, j) = 0


• OPT(i, 0) = 0


**Case 1: The current characters match**


• A[i - 1] = B[j - 1]


• Add the value of the current matching to other matching characters


**Case 2: The current characters do not match**


• A[i - 1] != B[j - 1]


• Ignore the last character of A or the last character of B and keep the HVLCS for the one that is being kept

<img width="819" height="237" alt="Screenshot 2026-04-05 at 10 08 01 PM" src="https://github.com/user-attachments/assets/4cb676ac-caa3-4e9d-9b23-3814eab46e9b" />

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
