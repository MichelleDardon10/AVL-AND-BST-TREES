from avl import AvlTree
from bst import BinarySearchTree
import random
import time

# Instantiate both Trees
avl = AvlTree()
bst = BinarySearchTree()


# Inserts
print("--------- Inserting elements to the Tree ---------")

def random_nodes(bst: BinarySearchTree, avl: AvlTree):
    numbers = random.sample(range(1, 1000001), 1000000)
    for num in numbers:
        bst.insert(num)
        avl.insert(num)
random_nodes(bst, avl)

# Traverse
print("--------- Traversing Tree ---------")
#bst.traverse(bst.root)

'''
# Search
print("--------- Searching keys in the Trees ---------")
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
print("--------- Searching for min-max in Trees ---------")


# Delete
print("--------- Deleting elements from the Trees ---------")
'''

print("--------- Visualization of the Trees ---------")
'''
avl.traverse(avl.root)
avl.traverse_and_add_nodes_to_the_graph(avl.root)
avl.display()

bst.traverse(bst.root)
bst.traverse_and_add_nodes_to_the_graph(bst.root)
bst.display()
'''