from avl import AvlTree
from bst import BinarySearchTree

#from graphviz import render
#import random
import time

# Instantiate both Trees
avl = AvlTree()
bst = BinarySearchTree()


# Inserts
#print("--------- Inserting elements to the Tree ---------")
for i in range(1,10):
    avl.insert(i)
    bst.insert(i)
#print("curret root: {}".format(avl.root))


# Traverse
print("--------- Traversing Tree ---------")
#bst.traverse(bst.root)
avl.traverse(avl.root)

'''
# Search
print("--------- Searching keys in the Tree ---------")
test_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#BENCHMARK SEARCH FUNCTION
#start_time= time.time()
for key in test_keys:
    print('Searching for {}: {}'.format(key, avl.search(key)))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time in ALV TREE: {elapsed_time:.6f} seconds")

print(avl)

print("-------------------------------")

start_time= time.time()
for key in test_keys:
    print('Searching for {}: {}'.format(key, bst.search(key)))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time in BST TREE: {elapsed_time:.6f} seconds")
print(bst)

# Min-Max 
print("--------- Searching for min-max in Tree ---------")


# Delete
print("--------- Deleting elements from the Tree ---------")
'''