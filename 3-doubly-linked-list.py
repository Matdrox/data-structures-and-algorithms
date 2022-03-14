class Node:
  def __init__(self, value):
    self.value = value
    self.next, self.prev = None

class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head, self.tail = new_node
    self.length = 1

my_doubly_linked_list = DoublyLinkedList(7)