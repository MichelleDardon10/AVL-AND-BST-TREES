from avl import AvlTree
from bst import BinarySearchTree
from graphviz import render
import random

# Instantiate both Trees
avl = AvlTree()
bst = BinarySearchTree()


# Inserts
print("--------- Inserting elements to the Tree ---------")
for i in range(1,10):
    avl.insert(i)
    bst.insert(i)
print("curret root: {}".format(avl.root))


# Traverse
print("--------- Traversing Tree ---------")


# Search
print("--------- Searching keys in the Tree ---------")
test_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for key in test_keys:
    print('Searching for {}: {}'.format(key, avl.search(key)))

# Min-Max 
print("--------- Searching for min-max in Tree ---------")


# Delete
print("--------- Deleting elements from the Tree ---------")
