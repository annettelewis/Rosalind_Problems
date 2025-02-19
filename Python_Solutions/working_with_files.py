# working with files: https://rosalind.info/problems/ini5/

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. 
        # Assume 1-based numbering of lines

with open("./Problem_Files/rosalind_ini5.txt", "r") as o:
    file = o.read().splitlines()[1::2]
    file_clean = "\n".join(file)
print(file_clean)