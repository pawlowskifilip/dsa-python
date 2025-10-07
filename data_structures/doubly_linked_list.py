class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insertNodeAtEnd(self, newNode):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = newNode
        newNode.prev = current_node

    def insertNodeAtMiddle(self, targetNode, newNode):
        if targetNode.next is None:
            return print("Try inserting at end")
        else:
            newNode.next = targetNode.next
            newNode.prev = targetNode

            targetNode.next.prev = newNode
            targetNode.next = newNode

    def searchByData(self, target_data):
        if not target_data:
            return print("No data passed in")

        current_node = self.head

        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.next

    def deletingHead(self):
        if not self.head:
            print("List is empty")

        current_node = self.head
        self.head = current_node.next
        current_node = None

    def deletingGivenNode(self, target_data):
        current_node = self.head

        if current_node.data == target_data:
            self.deletingHead()
            return

        while current_node and current_node.data != target_data:
            current_node = current_node.next

        if current_node is None:
            print("data not found in a list")
            return

        current_node.prev.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = current_node.prev
        current_node = None


doubly_linked_list = DoublyLinkedList()
ten = Node(10)
twenty = Node(20)
thirty = Node(30)
five = Node(5)
doubly_linked_list.insertNodeAtHead(five)
doubly_linked_list.insertNodeAtEnd(ten)
doubly_linked_list.insertNodeAtEnd(thirty)
# doubly_linked_list.insertNodeAtMiddle(ten, twenty)
# doubly_linked_list.printLinkedList()
# print(doubly_linked_list.searchByData(10).next.data)
# doubly_linked_list.deletingHead()
doubly_linked_list.deletingGivenNode(10)
doubly_linked_list.printLinkedList()
