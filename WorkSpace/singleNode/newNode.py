class Node(object):
    """Node"""
    elem = None
    next = None

    def __init__(self, elem):
        self.elem = elem
        self.next = None

    # node = Node(100)
class singleLinkList(object):
    """single Linked List """

    def __init__(self, node=None):
        self.__head = node
        pass

    def isempty(self):
        """Linked List is None or Not"""
        return self.__head == None
        pass

    def length(self):
        """Linked List's Length"""
        """current用以设置游标 以便遍历链表"""
        count = 0
        current = self.__head
        """current current.next 前者判断当前，后者判断之后，前者起始点为0，后者为1"""
        while current != None:
            count = count + 1
            current = current.next

        return count
        pass

    def travel(self):
        """Print All """
        list = []
        curr = self.__head
        while curr != None:
            list.append(curr.elem)
            curr = curr.next
        return list
        pass

    def add(self, elem):
        """Add Fist Node on the List"""
        node = Node(elem)
        if self.isempty():
            self.__head = node
        else:
            curr = self.__head
            self.__head = node
            node.next = curr
            del curr
            del node

        pass

    """"""
    def append(self, elem):
        """Add Last Node on the List"""
        node = Node(elem)

        if self.isempty():
            self.__head = node

        else:
            curr = self.__head
            '''找到最后一个节点，而不是到Node节点'''
            while curr.next != None:
                curr = curr.next

            curr.next = node
        pass

    def insert(self, index, elem):
        """Add index's Node on the List"""
        if index > self.length():
            print("error")
        elif index == 0:
            self.add(elem)
        elif index == self.length()-1:
            curr = self.__head
            while curr.next.next != None:
                curr = curr.next
            node = Node(elem)
            node.next = curr.next
            curr.next = node

            # print(curr.elem)
        else:
            curr = self.__head
            while (index-1):
                curr = curr.next

            # print(curr.elem)
            node = Node(elem)
            node.next = curr.next
            curr.next = node
        pass

    def remove(self, item):
        """delete node"""

        pass

    def search(self, item):
        """find item is None or Not"""

        pass

n = Node(5)
s = singleLinkList(node=n)

s.add(3)
s.append(7)
# s.insert(2,6)
l = s.travel()
print(l)
print("length:%d"%s.length())
s.insert(1,4)
l = s.travel()
print(l)
print("length:%d"%s.length())
s.insert(3,6)
l = s.travel()
print(l)
print("length:%d"%s.length())
s.insert(0,2)
l = s.travel()
print(l)
print("length:%d"%s.length())