# Rabbits and Reccurrence Relations: https://rosalind.info/problems/fib/

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, 
        # if we begin with 1 pair and in each generation, every pair of reproduction-age 
        # rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
with open("./Problem_Files/rosalind_fib.txt") as data:
           separate = data.read().split()
           n = int(separate[0]) # number of pairs after n months
           k = int(separate[1]) # rabbit pairs produced

def rabbit_checker(n, k):
    if n in {0, 1}: # default to return n
        return n 
    return rabbit_checker(n-1, k) + k * rabbit_checker(n-2, k)

#[rabbit_checker(n,k) for n in range(15)] # see Fibonacci seq

rabbit_checker(n, k)