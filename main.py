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
'''
for i in range(1,10):
    avl.insert(i)
    bst.insert(i)
#print("curret root: {}".format(avl.root))
'''
bst.insert(50)
bst.insert(20)
bst.insert(26)
bst.insert(12)
bst.insert(100)
bst.insert(90)
bst.insert(101)

avl.insert(50)
avl.insert(20)
avl.insert(26)
avl.insert(12)
avl.insert(100)
avl.insert(90)
avl.insert(101)

# Traverse
print("--------- Traversing Tree ---------")
#bst.traverse(bst.root)
avl.traverse(avl.root)
avl.traverse_and_add_nodes_to_the_graph(avl.root)
avl.display()

bst.traverse(bst.root)
bst.traverse_and_add_nodes_to_the_graph(bst.root)
bst.display()
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