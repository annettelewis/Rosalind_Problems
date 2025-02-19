# Transcribing DNA into RNA: https://rosalind.info/problems/rna/

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.
with open("./Problem_Files/rosalind_rna.txt", "r") as r:
    sequence = r.read().replace("T", "U")
    print(sequence)