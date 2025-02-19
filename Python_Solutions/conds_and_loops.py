# conditions and loops: https://rosalind.info/problems/ini4/

# Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.
with open("./Problem_Files/rosalind_ini4.txt", "r") as w:
    file = w.read().split()

file_int = [int(i) for i in file] # convert str to int

start, end = file_int

sum_odd = 0 # initializing the sum of odd integers

for i in range(start, end): # sum of odd integers
    if i % 2 == 1:
        sum_odd += i
        
print(sum_odd)