# Counting DNA Nucleotides: https://rosalind.info/problems/dna/

# Given: A DNA string s of length at most 1000 nt. 

# Return: Four integers (separated by spaces) counting the respective number 
        # of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def nucleotide_count(sequence):
    A = sequence.count("A")
    C = sequence.count("C")
    G = sequence.count("G")
    T = sequence.count("T")
    print(A, C, G, T)

with open("./Problem_Files/rosalind_dna.txt", "r") as r:
    sequence = r.read()
    nucleotide_count(sequence)