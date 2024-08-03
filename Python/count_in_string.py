'''
Problem
You are given a string S containing lowercase English alphabets and a character k.  

Task

Count the number of occurrences of k in S.

Example

Assumptions

S = "abdbs"
k = "b"
Approach

You can see that the number of occurrences of b in S is 2. Hence, the answer is 2.
Function description

Complete the solve function which takes a string S and a character k as the argument and returns the number of occurrences of k in S:

S: Represents the string
k: Represents the character
Input format

Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).

The first line contains a single integer T, which denotes the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
For each test case:
The first line contains a string S.
The second line contains the character k.
Output format

For each test case, print a single line representing the number of occurrences of k in S.

Constraints


Sample Input
1
andadds
d
Sample Output
3
Time Limit: 2
Memory Limit: 256
Source Limit:
Explanation
Given

The first line represents the number of test cases, T=1.

S = "andadds"
k = "d"
Approach

Since the number of occurrences of "d" in S is 3, the answer is 3.
'''

def solve (S, k):
    return S.count(k)

T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print (out_)