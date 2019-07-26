import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n") 
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

duplicates = []
binarySearchTree = None

for first in names_1:
    if binarySearchTree is None:
        binarySearchTree = BinarySearchTree(first)
    else:
        binarySearchTree.insert(first)
for second in names_2:
    if binarySearchTree.contains(second):
        duplicates.append(second)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")