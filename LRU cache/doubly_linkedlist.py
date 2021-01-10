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
	def insert(self,val):
		new_node = node(val)
	
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


d = DLL()
d.insert(1)
d.insert(2)
d.insert(3)
d.insert(4)
d.delete_by_node(d.head)
d.print_DLL()




	
		
		
		

		