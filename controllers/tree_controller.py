from models.binary_search_tree import (
    BinarySearchTree,
    TreeDepthLimitError,
    DuplicateValueError
)


class TreeController:

    def __init__(self, view):
        self.tree = BinarySearchTree(max_levels=4)
        self.view = view

    def add_node(self):

        raw_value = self.view.get_input_value()

        try:
            value = int(raw_value)

            self.tree.insert(value)

            self.view.update_tree(
                self.tree.root,
                self.tree.preorder(),
                self.tree.inorder(),
                self.tree.postorder()
            )

            self.view.clear_input()

            self.view.show_success(
                f"Node {value} added successfully."
            )

        except ValueError:
            self.view.show_error(
                "Invalid input. Please enter an integer."
            )

        except DuplicateValueError as error:
            self.view.show_error(str(error))

        except TreeDepthLimitError as error:
            self.view.show_error(str(error))

    def search_node(self):

        raw_value = self.view.get_input_value()

        try:
            value = int(raw_value)

            result = self.tree.search(value)

            if result is not None:
                self.view.show_success(
                    f"Node {value} was found in the tree."
                )
            else:
                self.view.show_info(
                    f"Node {value} does not exist in the tree."
                )

        except ValueError:
            self.view.show_error(
                "Invalid input. Please enter an integer."
            )

    def clear_tree(self):

        self.tree.clear()

        self.view.update_tree(
            self.tree.root,
            self.tree.preorder(),
            self.tree.inorder(),
            self.tree.postorder()
        )

        self.view.clear_input()

        self.view.show_success(
            "Tree cleared successfully."
        )

    def exit_application(self):

        self.view.close()