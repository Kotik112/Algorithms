class Node:
    def __int__(self, data: str):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def traversal(self):
        # first: Node = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data: Node):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find_node(self, data_to_find):
        key = self.head
        while key is not None:
            if key.data == data_to_find:
                return True
            key = key.next
        return False


if __name__ == '__main__':
    node = Node(1)
    family = LinkedList()
    family.head = Node("Arman")
    wife = Node("Myra")
    first_kid = Node("Lilly")
    second_kid = Node("Martin")

    family.head.next = wife
    wife.next = first_kid
    first_kid.next = second_kid

    family.traversal()
