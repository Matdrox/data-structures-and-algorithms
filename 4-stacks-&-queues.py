class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:      # Last in, first out
  def __init__(self, value):
    new_node = Node(value)
    self.top = new_node
    self.height = 1

  def print_stack(self):
    temp = self.top
    while temp != None:
      print(temp.value)
      temp = temp.next

  def push(self, value):
    new_node = Node(value)
    if self.height == 0:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
      self.height += 1

  def pop(self):
    if self.height == 0:
      return None
    temp = self.top
    self.top = self.top.next
    temp.next = None
    self.height -= 1
    return temp

# my_stack = Stack(4)
# my_stack.push(3)
# my_stack.push(2)
# my_stack.push(1)
# my_stack.print_stack()

# print(f"\n{my_stack.pop()}\n")

# my_stack.print_stack()
# print(f"\n{my_stack.push(3)}\n")
# print(f"\n{my_stack.pop()}\n")


class Queue:
  def __init__(self, value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

  def print_queue(self):
    temp = self.first
    while temp != None:
      print(temp.value)
      temp = temp.next

  def enqueue(self, value):
    new_node = Node(value)
    if self.first == None:
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1

  def deqeue(self):
    if self.length == 0:
      return False
    temp = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = self.first.next
      temp.next = None
    self.length -= 1
    return temp

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()