# counting point mutations: https://rosalind.info/problems/hamm/

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

# function
def hamming_dist(s:str, t:str) -> int:
    """Find the Hamming distance (d_H(s,t)), or count of point mutations, between two strings of equal length

    Args:
        s (str): A nucleotide sequence
        t (str): A nucleotide sequence

    Returns:
        int: Count of mismatches representing the Hamming distance value
    """
    count = 0 # initializing counter
    if len(s) != len(t):
        raise ValueError("Sequences must have the same length.")

    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

# clean and read in file
with open("./Problem_Files/rosalind_hamm.txt") as o:
    separate = o.read().split("\n")
    s = separate[0]
    t = separate[1]

print(hamming_dist(s, t))