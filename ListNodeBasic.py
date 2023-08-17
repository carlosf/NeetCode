class ListNode:

  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = ListNode(
      -1
    )  # -1 is a secial value to determine that there is an empty linked list
    self.tail = self.head  #set the last ListNode to be the same as the first ListNode

  '''
  Lets insert a new ListNode at the end - this should be O(1)
  '''

  def insertEnd(self, val):
    self.tail.next = ListNode(val)  #add a node at the end
    self.tail = self.tail.next  #set the pointer to the last ListNode to the newly created ListNode

  '''
  Remove a linked list
  '''

  def remove(self, index):
    i = 0
    curr = self.head
    while i < index and curr:  #find he element before you want to delete (checks for curr as it make sure it stops a null or None)
      i += 1
      curr = curr.next

    if curr and curr.next:  #check to see if not null
      if curr.next == self.tail:  #check to see if last
        self.tail = curr
      curr.next = curr.next.next

  '''
  Print the linked list to console
  '''

  def print(self):
    curr = self.head.next  #first element is actually -1 - this will actually point to the first element in the list
    while curr:  #will stop when None?
      print(curr.val, "->", end="")  #not sure of what the end is for
      curr = curr.next
    print()


x = LinkedList()
x.insertEnd("1")
x.insertEnd("2")
x.insertEnd("3")
x.print()
x.remove(1)
x.print()
