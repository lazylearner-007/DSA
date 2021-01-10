# from doubly_linkedlist import *

class node:
	"""docstring for DDL"""
	def __init__(self,val):
		self.value = val
		self.next = None
		self.prev = None

class DLL:
	"""docstring for DDL"""
	def __init__(self):
		self.head = None
		self.tail = None

	#insert at the end
	def insert(self,new_node):
		
		if not self.head:
			self.head = new_node
			self.tail = new_node
			self.head.next = self.tail
			return

		self.tail.next = new_node
		new_node.prev = self.tail

		self.tail = new_node
		self.tail.next = None

	def delete_by_node(self,node):
		if not node.prev:
			self.head = node.next
		if node.prev:
			node.prev.next = node.next 
		if node.next:
			node.next.prev = node.prev 

	def print_DLL(self):
		if not self.head:
			return "Empty DLL"
		head = self.head
		while(head):
			print(head.value)
			head = head.next

	
class LRU:
	"""docstring for LRU"""
	def __init__(self,capacity):
		self.capacity = capacity
		self.dict = {}
		self.DLL = DLL()

	def get(self,item):
		try:
			LRU_node = self.dict[item]
			self.DLL.delete_by_node(LRU_node)
			self.DLL.insert(LRU_node)
			return LRU_node.value		
		except:
			return -1
		
	def put(self,key):
		new_node = node(key)

		if len(self.dict) >= self.capacity:
			head = self.DLL.head
			self.dict.pop(head.value)
			self.DLL.delete_by_node(head)
		
		self.DLL.insert(new_node)
		self.dict[key] = new_node



l= LRU(4)
l.put(1)
l.put(2)
l.put(3)
l.put(4)
l.put(5)
l.get(2)
l.put(3)
l.DLL.print_DLL()





