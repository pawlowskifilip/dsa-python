class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
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
        current_node.setNext(newNode)

    def insertNodeAtMiddle(self, targetNode, newNode):
        if targetNode.getNext is None:
            return print("Try inserting at end")
        else:
            newNode.setNext(targetNode.next)
            targetNode.setNext(newNode)

    def searchByData(self, target_data):
        if not target_data:
            return print("No data passed in")

        current_node = self.head
        while current_node:
            if current_node.getData() == target_data:
                return current_node
            current_node = current_node.getNext()

    def deletingHead(self):
        current_node = self.head
        self.head = current_node.getNext()
        current_node = None

    def deletingGivenNode(self, target_data):
        current_node = self.head
        if current_node.getData() == target_data:
            self.deletingHead()

        previous_node = None

        while current_node and current_node.getData() != target_data:
            previous_node = current_node.getData()
            current_node = current_node.getNext()

        if current_node.getNext() is None:
            return print("data not found")

        else:
            previous_node.setNext(current_node.getNext())


linked_list = LinkedList()
ten = Node(10)
twenty = Node(20)
thirty = Node(30)
five = Node(5)
linked_list.insertNodeAtHead(ten)
linked_list.insertNodeAtEnd(twenty)
linked_list.insertNodeAtEnd(thirty)
linked_list.insertNodeAtHead(five)
# linked_list.insertNodeAtMiddle(twenty, Node(25))
linked_list.printLinkedList()
print("=====")
linked_list.deletingHead()
linked_list.printLinkedList()
# target_node = linked_list.searchByData(10)
# print(target_node.getNext().getData())
