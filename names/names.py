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
# "line in file" runtime is O(log n), which is nested within a for loop O(n), therefor...
#   Runtime here would be O(n) * O(log n) -> O(n log n)
with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
        f2 = f2.read().splitlines()
        duplicates = []
        # O(n) * O(log n) = O(n log n)
        for line in f1.read().splitlines(): # O(n)
            if line in f2:                  # O(log n)
                duplicates.append(line)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {(end_time - start_time) * 1000} milliseconds")

