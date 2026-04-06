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

**Data**


| File Number | Runtime (in seconds) |
| ----------- | -------------------- |
| 1 | 0.000091 |
| 2 | 0.000122 |
| 3 | 0.000065 |
| 4 | 0.000074 |
| 5 | 0.000099 |
| 6 | 0.000066 |
| 7 | 0.000082 |
| 8 | 0.000072 |
| 9 | 0.000129 |
| 10 | 0.000141 |


**Graph**


<img width="606" height="370" alt="Screenshot 2026-04-05 at 10 40 09 PM" src="https://github.com/user-attachments/assets/f9c09d6c-dc95-4a19-b76a-77a6adbae357" />


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


**Explanation of Recurrence:**


The base case is correct because if either string A or B has a length of 0, then there is no possibiility of there being a common subsequence as there is at least one string from the two that's non-existent. Additionally, this base case covers the possibility of both strings having a length of 0 since either equation (i = 0 or j = 0) ensures that all cases where either string is non-existent is covered, thus covering the case where both would be 0. 


The case where "the current characters match" is correct because, since the characters match you can include them in the subsequence, and any subsequence that uses these current characters must come from the pair (i - 1, j - 1). Therefore, you are building the solution upon smaller subproblems.


Lastly, the case where "the current characters do not match" is correct because since the characters don't match, you must either ignore A[i - 1] of B[j - 1] since any valid common subsequence cannot include at least one of these current characters. Therefore, the optimal solution must already exist in one of these two smaller subproblems; the max just makes sure you pick the larger value which will maxmixe the total resulting value.


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
