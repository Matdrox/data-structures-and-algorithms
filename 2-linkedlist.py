head = {
  "value": 11,
  "next": {
    "value": 3,
    "next": {
      "value": 23,
      "next": {
        "value": 7,
        "next": None
      }
    }
  }
}

# print(head['next']['next']['value'])

# This will only run with a Linked List
# print(my_linked_list.head.next.next.value)


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
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
    if self.head == None:             #Check if LL is empty
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail
    self.length += 1
    return True

  # def prepend(self, value):

  # def inset(self, index, value):


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()