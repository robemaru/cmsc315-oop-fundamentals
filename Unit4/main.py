"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive helper compares the new value with each node.
        # Smaller values belong on the left; larger values belong on the right.
        # This ordering keeps values organized and reduces the search space.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position is where the new node belongs.
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values are placed in the left subtree.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values are placed in the right subtree.
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values are ignored so each employee ID remains unique.
            return node

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST search can eliminate an entire subtree after each comparison.
        # In a balanced tree, this makes the average search time O(log n),
        # compared with O(n) for a linear search through an unsorted list.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching None means the value is not in the tree.
        if node is None:
            return False

        if value == node.value:
            return True
        if value < node.value:
            # The value can only be in the left subtree.
            return self._search_recursive(node.left, value)

        # The value can only be in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visiting left, current, then right produces ascending order
        # because the BST stores smaller values to the left and larger
        # values to the right.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Real-world scenario: employee records organized by employee ID.
    # The employee IDs are numeric keys, so the BST can quickly narrow
    # the search to the left or right subtree after each comparison.
    employee_ids = [1001, 1050, 1005, 1025, 1010, 1075, 1035, 1100]
    tree = BST()

    for employee_id in employee_ids:
        tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)
    print("BST root:", tree.root.value)
    print("The BST reduced the search space by choosing only the left or right subtree after each comparison.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_ids = tree.inorder()
    print("Employee IDs in sorted order:", sorted_ids)
    # In-order traversal visits left, current, and right, so the BST's
    # ordering causes the employee IDs to be returned in ascending order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    existing_ids = [1025, 1100]
    missing_ids = [999, 1200]

    for employee_id in existing_ids:
        print(f"Search for employee ID {employee_id}: {tree.search(employee_id)} (found)")

    for employee_id in missing_ids:
        print(f"Search for employee ID {employee_id}: {tree.search(employee_id)} (not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: an empty tree can be traversed safely and returns an empty list.
    empty_tree = BST()
    print("Empty tree in-order traversal:", empty_tree.inorder())
    print("Search in empty tree for 1001:", empty_tree.search(1001))

    # Edge case 2: duplicate employee IDs are ignored because employee IDs
    # should be unique in this real-world scenario.
    tree.insert(1025)
    print("After inserting duplicate ID 1025:", tree.inorder())

    # Edge case 3: a single-node tree still supports insertion, traversal, and search.
    single_tree = BST()
    single_tree.insert(2000)
    print("Single-node tree traversal:", single_tree.inorder())
    print("Search for 2000 in single-node tree:", single_tree.search(2000))

    print("\n=== SUMMARY ===")
    print("BST example: employee records organized by employee ID.")
    print("The tree supports recursive insertion and searching, and in-order traversal returns sorted IDs.")
    print("A balanced BST has average O(log n) search/insert performance, while a highly unbalanced BST can become O(n).")


if __name__ == "__main__":
    main()
