import main


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def head(self, val):
        self.data = val


class LinkedList:


    def __init__(self):
        self.head = None


    def is_empty(self):
        if self.head:
            return False
        return True



    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node



    def append(self, val, ):
        if self.is_empty():
            curennt = self.head
            while curennt.next:
                if curennt.next is None:
                    curennt.next = Node(val)
                else:
                    curennt = curennt.next



    def del_fir(self):
        curent = self.head
        self.head = curent.next


    def del_after(self, node):
        curent = self.head
        while curent:
            if curent == node:
                curent2 = curent.next
                curent.next = curent2.next
            else:
                curent = curent.next



    def find(self, val):
        curent = self.head
        while curent:
            if curent.data == val:
                return curent.data
            curent = curent.next
        return None


    def length(self):
        counter = 0
        current = self.head
        while current:
            current = current.next
            counter += 1
        return counter



    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def find_index(self):
        pass



if __name__ == "__main__":
    print("=== הוספת איברים ===")
    lst.push(10)
    lst.push(20)
    lst.push(30)


