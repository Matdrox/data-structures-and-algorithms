# Binary Search Trees (BST) work in 2ⁿ => O(log(n)). Very efficient, divide and conquer
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node
      return True
    temp = self.root
    while True:
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right

  def contains(self, value):
    temp = self.root
    while temp != None:
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True
    return False

  def min_value(self, current_node):
    while current_node.left != None:
      current_node = current_node.left
    return current_node.value

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(53)
my_tree.insert(13)
my_tree.insert(24)
my_tree.insert(63)
my_tree.insert(20)
print(my_tree.min_value(my_tree.root))

# print(my_tree.contains(22))
# print(my_tree.root.value)