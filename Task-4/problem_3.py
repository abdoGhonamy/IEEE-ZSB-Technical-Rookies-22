# creation of node which is a subclass to the linked list class
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
# creation of linked list
class Linkedlist:
    def __init__(self):
        # head is the first node in the list
        self.head = node()

    # to append data in the last of the list
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    # to add data in the end of the list
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    # to get the length of the list
    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    # to delete the data of a certain index

    def erase(self, index):
        if index >= self.length():
            print("ERORR: erase index is out of rane")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1
