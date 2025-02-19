# dictionaries: https://rosalind.info/problems/ini6/

# Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s, where words are separated by spaces. 
        # Words are case-sensitive, and the lines in the output can be in any order.
s = "We tried list and we tried dicts also we tried Zen"

words = {}
with open("./Problem_Files/rosalind_ini6.txt", "r") as o:
    for word in o.read().split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

for key, value in words.items():
    print(key, value)