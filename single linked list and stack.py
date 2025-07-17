#implement a singly linked list in python with node class ?(data , next ) and methods :
#insert a front and end
#delete at front and traverse
#implement a stack using a linked list with push , pop, peek , and is empty
 #   test linked list :insert [10,20,30],delete front .test stack :push[5,10],pop once, peek
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        self.head = Node(data, self.head)

    def insert_end(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def traverse(self):
        vals, curr = [], self.head
        while curr:
            vals.append(curr.data)
            curr = curr.next
        return vals

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.insert_front(data)

    def pop(self):
        if self.is_empty(): return None
        val = self.list.head.data
        self.list.delete_front()
        return val

    def peek(self):
        return None if self.is_empty() else self.list.head.data

    def is_empty(self):
        return self.list.head is None

# 🔹 Test LinkedList
ll = LinkedList()
for val in [10, 20, 30]:
    ll.insert_end(val)
print("Linked List:", ll.traverse())
ll.delete_front()
print("After deleting front:", ll.traverse())

# 🔹 Test Stack
s = Stack()
s.push(5)
s.push(10)
print("\nStack Peek:", s.peek())
print("Stack Pop:", s.pop())
print("Stack Peek after Pop:", s.peek())

