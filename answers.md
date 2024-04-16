# CMPS 2200 Assignment 3
## Answers

**Name:** Isaac Ratzan


1a) For a given amount N, choose the largest denomination (2^k) that fits within N each time until N goes down to 0.

1b) To find the optimal amount, find the highest denomination ≤ N iteratively. This greedy approach ensures the least amount of coins used. It is optimal because the solutions are solved through subproblem solutions, thus preserving optimal substructure properties where d > 2^k.

1c) Work = O(log (n)), Span = O(1).

2a) In a scenario where N=6 and there are denominations of {1, 4}, choosing 4 yields 2 coins, but it would be optimal to use 3 coins of denomination 1.

2b) True because analyzing the denominations at each step allows the minimum number of coins used.

2c) Work = O(nk) and Span = O(nk) with k being the number of denominations.