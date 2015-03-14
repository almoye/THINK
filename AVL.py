import math

elements = [1, 4, -5, 8, 9, 11, 4, 5, 0]


class TreeNode():
    def __init__(self, element=0, depth=0):
        self.element = element
        self.parent = None
        self.left = None
        self.right = None
        self.depth = depth


class RootNode():
    def __init__(self):
        self.next = None


class AvlTree():
    def __init__(self):
        self.root = RootNode()

    def is_balance(self, tree):
        if tree is None:
            return True
        left_depth = 0
        while tree.left is not None:
            left_depth += 1
            tree = tree.left
        right_depth = 0
        while tree.right is not None:
            right_depth += 1
            tree = tree.right
        if math.fabs(left_depth - right_depth) > 1:
            return False
        return True

    def left_or_right(self, tree):
        left_depth = 0
        right_depth = 0
        while tree.left is not None:
            left_depth += 1
            tree = tree.left
        while tree.right is not None:
            right_depth += 1
            tree = tree.right

        if left_depth > right_depth:
            return "left"
        elif right_depth > left_depth:
            return "right"

    def insert(self, element, depth):
        if self.root.next is None:
            node = TreeNode(element, depth)
            node.parent = self.root
            self.root.next = node
            return

        tree = self.root.next
        while tree is not None:
            depth += 1
            temp_tree = tree
            if self.is_balance(temp_tree) is False:
                print "need reset"
                self.inorder(temp_tree)
                #self.left_rotate(temp_tree)
                if self.left_or_right(temp_tree) == "right":
                    self.left_rotate(temp_tree)
                elif self.left_or_right(temp_tree) == "left":
                    self.right_rotate(temp_tree)
                print "--------"
                self.inorder(temp_tree)
            if tree.element >= element:
                tree = tree.left
            elif tree.element < element:
                tree = tree.right
        node = TreeNode(element, depth)
        node.parent = temp_tree
        if temp_tree.element >= element:
            temp_tree.left = node
        elif temp_tree.element < element:
            temp_tree.right = node

    def left_rotate(self, tree):
        if tree.right is None:
            return
        node = tree.right
        tree.right = node.left
        if node.left is not None:
            node.left.parent = tree
            node.parent = tree.parent
        if tree.parent is self.root:
            self.root.next = node
        elif tree is tree.parent.left:
            tree.parent.left = node
        else:
            tree.parent.right = node
            node.left = tree
            tree.parent = node

    def right_rotate(self, tree):
        if tree.left is None:
            return
        node = tree.left
        tree.left = node.right
        if node.right is not None:
            node.right.parent = tree
        node.parent = tree.parent
        if tree.parent is self.root:
            self.root.next = node
        elif tree is tree.parent.right:
            tree.parent.right = node
        else:
            tree.parent.left = node
        node.right = tree
        tree.parent = node

    def inorder(self, tree):
        if tree is None:
            return
        self.inorder(tree.left)
        print "-----------"
        print "element is ", tree.element, "depth is ", tree.depth
        self.inorder(tree.right)


tree = AvlTree()
for i in elements:
    tree.insert(i, 0)