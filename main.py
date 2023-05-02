from avl import AVLTree
from bst import BinarySearchTree
import random
import time

# Instantiate both Trees
avl = AVLTree()
bst = BinarySearchTree()

x = 1001
y = 1000

# Inserts
print("--------- Inserting elements to the Tree ---------")

def random_nodes(bst: BinarySearchTree, avl: AVLTree):
    numbers = random.sample(range(1, x), y)
    
    for num in numbers:
        bst.insert(num)
        avl.insert(num)
random_nodes(bst, avl)

# Traverse
print("--------- Traversing Tree ---------")
bst.traverse(bst.root)
avl.traverse(avl.root)


# Search
print("--------- Searching keys in the Trees ---------")

test_numbers = random.sample(range(1, x), y)

#BENCHMARK SEARCH FUNCTION
start_time= time.time()
for key in test_numbers:
    print('Searching for {}: {}'.format(key, avl.search(key)))
end_time = time.time()
elapsed_time1 = end_time - start_time
print(f"Elapsed time in AVL TREE: {elapsed_time1:.6f} seconds")

#print(avl)

print("-------------------------------")

start_time= time.time()
for key in test_numbers:
    print('Searching for {}: {}'.format(key, bst.search(key)))
end_time = time.time()
elapsed_time2 = end_time - start_time
print(f"Elapsed time in BST TREE: {elapsed_time2:.6f} seconds")

diferencia = elapsed_time2 - elapsed_time1
print("La diferencia fue de: ", diferencia)

# Min-Max 
print("--------- Searching for min-max in Trees ---------")
print(avl.find_max(avl.root))
print(avl.find_min(avl.root))
print(bst.find_min(bst.root))
print(bst.find_max(bst.root))


# Delete
print("--------- Deleting elements from the Trees ---------")
for i in range (5):
    x = test_numbers[random.randint(0,y)]
    print(avl.delete(x))
    print(bst.delete(x))


print("--------- Visualization of the Trees ---------")

dot = avl.to_graphviz()
dot.render("AVL-TREE.gv", view=True)


bst.traverse_and_add_nodes_to_the_graph(bst.root)
bst.display()
