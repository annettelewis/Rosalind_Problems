# Computing GC Content: https://rosalind.info/problems/gc/

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content 
        # of that string. Rosalind allows for a default error of 0.001 in all decimal answers 
        # unless otherwise stated; please see the note on absolute error below.

# functions
def GC_content(seq):
    G = seq.count("G")
    C = seq.count("C")
    total = len(seq)
    return round((G+C)/total*100, 6) # mult by 100 (%)

# initialize dictionary
seqs = {}

# open and clean file
with open("./Problem_Files/rosalind_gc.txt") as f:
    separate = f.read().split(">")[1:] # get rid of ""
    for i in separate:
        clean = i.split("\n") # display all of the parts in a sequence still has empty string
        seq = "".join(clean[1:]).strip()
        seqs[clean[0]] = GC_content(seq) # fill dict w/ id: gc_content

# now we want to get the seq with the most GC content
max_id = max(seqs, key=seqs.get)
max_gc = seqs[max_id]

print(f"{max_id}\n{max_gc}")