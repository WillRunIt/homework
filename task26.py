class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data):
        current_node = self.head
        if current_node is None:
            return
        if current_node.data == data:
            self.head = current_node.next
            return
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def selection_sort(self):
        if self.head is None:
            return

        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next

linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(5)
linked_list.insert(1)
linked_list.insert(4)
linked_list.insert(2)

print("Original list:")
linked_list.print_list()

linked_list.selection_sort()

print("Sorted list:")
linked_list.print_list()