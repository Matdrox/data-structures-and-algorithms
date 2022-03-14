class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp != None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return True

  def pop(self):
    if self.length == 0:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      temp = self.tail
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev.next = None
    self.length -= 1
    return temp

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head == new_node
      self.tail == new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True

  def pop_first(self):
    if self.length == 0:
      return None
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      temp = self.head
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp

  def get_value(self, index):
    if index < 0 or index >= self.length:
      return None
    if index < self.length/2:     # Search in first half, starting from head
      temp = self.head
      for _ in range(index):
        temp = temp.next
    else:                         # Search in second half, starting from tail
      temp = self.tail
      for _ in range(self.length - 1, index, -1):     # Start from last index to index, decrement by 1
        temp = temp.prev
    return temp.value


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.print_list()

print(f"\n{my_doubly_linked_list.get_value(2)}\n")

my_doubly_linked_list.print_list()


# my_doubly_linked_list.pop()
# print(f"\n{my_doubly_linked_list.prepend(2)}\n")
# print(f"\n{my_doubly_linked_list.pop_first()}\n")