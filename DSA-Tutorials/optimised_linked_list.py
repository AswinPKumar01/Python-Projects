import unittest
from Linked_list import Node, LinkedList  # Adjust the import statement


class TestLinkedListMethods(unittest.TestCase):
    def test_node_creation(self):
        node = Node(42)
        self.assertEqual(node.data, 42)
        self.assertIsNone(node.next)

    def test_linked_list_creation(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)

    def test_append_and_display(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        # Test that append and display work as expected
        self.assertEqual(linked_list.display(), "1 -> 2 -> 3 -> None")

    def test_append_empty_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)

        # Test that appending to an empty linked list sets the head
        self.assertEqual(linked_list.head.data, 1)

    def test_append_non_empty_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)

        # Test that appending to a non-empty linked list adds a new element
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 2)

    def test_display_empty_linked_list(self):
        linked_list = LinkedList()

        # Test that displaying an empty linked list results in "None"
        self.assertEqual(linked_list.display(), "None")

if __name__ == "__main__":
    unittest.main()
