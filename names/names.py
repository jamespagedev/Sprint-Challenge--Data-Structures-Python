import time

start_time = time.time()

#------------------- Provided Solution O(n^2) -------------------
"""
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

#-------------- First Optomized Solution O(n log n) -------------
# "line in file" runtime is O(log n), which is nested within a for loop O(n), therefore...
#   Runtime here would be O(n) * O(log n) -> O(n log n)
"""
with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
        f2 = f2.read().splitlines()
        duplicates = []
        # O(n) * O(log n) = O(n log n)
        for line in f1.read().splitlines(): # O(n)
            if line in f2:                  # O(log n)
                duplicates.append(line)
"""

#--------------------------- MVP O(n) ---------------------------
# each file open is a single O(n) -> O(2n)
# since both files lines are being read at the same time O(2n)...
# We can conclude the final runtime formula is...
# O(4n) -> O(n)
"""
with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
    dict_names = {}
    for line1, line2 in zip(f1.read().splitlines(), f2.read().splitlines()):
            dict_names[line1] = line2

duplicates = []
for value in dict_names.values(): # O(n)
    if value in dict_names: # hash keys O(1)
        duplicates.append(value) # O(1)
"""

#------------------------- Stretch O(n) -------------------------
# Best solution
# Best runtime complexity
# Best space complexity
# set has the same space complexity of a list O(n)
# Space complexity uses a set rather than using a list and a dictionary, however,
#   since we are only storing duplicate values, the space used will be much less on average
# Since both a set and a list have space complexity O(n), this makes the space complexity the best
# Instead of storing 10,000 names in the list, we are only storing the duplicate names found in the set
# Therefore... this also has the best space complexity
with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
        duplicates = set(f1.read().splitlines()).intersection(f2.read().splitlines())

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {(end_time - start_time) * 1000} milliseconds")
