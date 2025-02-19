# Complementing a Strand of DNA: https://rosalind.info/problems/revc/

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement s^c of s.
complement = {"A":"T", "C":"G", "G":"C", "T":"A"}

with open("./Problem_Files/rosalind_revc.txt", "r") as r:
    sequence = r.read()
    reverse_complement = "".join(complement.get(base, base) for base in sequence)[::-1].strip("\n")
    print(reverse_complement)