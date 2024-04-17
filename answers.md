# CMPS 2200 Assignment 3
## Answers

**Name:** Isaac Ratzan


1a) For a given amount N, choose the largest denomination of (2^k) that fits within N each time and subtract N until it goes down to 0.

1b) To find the optimal amount, find the highest denomination ≤ N iteratively where k is the highest integer such that 2^k <= N. This greedy approach ensures the least amount of coins used. It is optimal because the solutions are solved through a binary nature with subproblem solutions, thus preserving optimal substructure properties where d > 2^k.

1c) Work = O(log (n)), Span = O(log(n)).

2a) In a scenario where N=4 and there are denominations of {1,2, 4}. The greedy scheduler would choose to take 2 2s rather than choosing the 4. 

2b) The optimal substructures means that the problem can be divided into the optimal solution to all of the subproblems This is true because analyzing the denominations at each step allows the minimum number of coins used. By adding one coin to the optimal solution, you can determine the optimal amount for N.

2c) 
change[d, n]:
   k = len(d)
   optimal[0] = 0
   for i in range (1, n):
      min = inf
      for j in range (1,k):
         if d[i] <= i:
            if (1+optimal[i-d[j]) < min:
               min = 1+optimal[i-d[j]
               coin = j
      optimal[i] = min
return optimal

Work = O(nk) and Span = O(N) with k being the number of denominations.