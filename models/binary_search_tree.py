from models.tree_node import TreeNode


class TreeDepthLimitError(Exception):
    pass


class DuplicateValueError(Exception):
    pass


class BinarySearchTree:

    def __init__(self, max_levels=4):
        self.root = None
        self.max_levels = max_levels
        self.node_count = 0

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
            self.node_count += 1
            return

        current = self.root
        level = 1

        while True:

            if value == current.value:
                raise DuplicateValueError(
                    f"Value {value} already exists."
                )

            if value < current.value:

                if current.left is None:

                    if level + 1 > self.max_levels:
                        raise TreeDepthLimitError(
                            "Maximum tree depth is 4 levels."
                        )

                    current.left = TreeNode(value)
                    self.node_count += 1
                    return

                current = current.left

            else:

                if current.right is None:

                    if level + 1 > self.max_levels:
                        raise TreeDepthLimitError(
                            "Maximum tree depth is 4 levels."
                        )

                    current.right = TreeNode(value)
                    self.node_count += 1
                    return

                current = current.right

            level += 1

    def search(self, value):

        current = self.root

        while current is not None:

            if value == current.value:
                return current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def preorder(self):

        result = []

        def traverse(node):

            if node is not None:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        return result

    def inorder(self):

        result = []

        def traverse(node):

            if node is not None:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)

        traverse(self.root)

        return result

    def postorder(self):

        result = []

        def traverse(node):

            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)

        traverse(self.root)

        return result

    def clear(self):

        self.root = None
        self.node_count = 0

    def get_height(self):

        def calculate_height(node):

            if node is None:
                return 0

            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            return 1 + max(left_height, right_height)

        return calculate_height(self.root)