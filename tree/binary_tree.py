import random

from collections import deque

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def traverse_inorder(self, root):
        if root.left:
            self.traverse_inorder(root.left)

        print root.data

        if root.right:
            self.traverse_inorder(root.right)

    def traverse_inorder_nonrecursive(self, root):
        node = root
        stack = []

        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                print node.data
                node = node.right


    def traverse_breadth_first(self, root):
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print node.data

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


if __name__ == "__main__":

    tree = BinaryTree()

    for i in range(1,10):
        tree.root = tree.insert(tree.root, random.randint(0, 20))

    print "\n\n"

    tree.traverse_inorder(tree.root)

    print "\n\n"

    tree.traverse_inorder_nonrecursive(tree.root)

    print "\n\n"

    tree.traverse_breadth_first(tree.root)

