# A utility class that represents an individual node in a BST
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key


# a utility function to insert a new node with the given key value
def insertnode(root,node):
	if root is None:
		root = node
	else:
		if root.val > node.val:
			if root.left is None:
				root.left = node
			else:
				insertnode(root.left,node)
		else:
			if root.right is None:
				root.right = node
			else:
				insertnode(root.right, node)


r = Node(50)
insertnode(r,Node(30))
insertnode(r,Node(20))
