# -*- mode:python-ts; -*-
# car-0 { prev: None,
#         value: 10,
#         next: car-1 { prev: car-0,
#                       value: 20,
#                       nxt: car-2 { prev: car-1,
#                                    value: 30,
#                                    nxt; car-3 { prev: car-2,
#                                                 value: 40,
#                                                 nxt: None }}}}
class DoubleLinkedListNode:
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f'[{repr(pval)} <- {self.value} -> {repr(nval)}]'


# Controller - Network
class DoubleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self.elements = 0

    def push(self, obj):
        """Append a new value on the end of the list."""
        if self.begin is None:
            dlln = DoubleLinkedListNode(obj, None, None)
            self.begin = dlln
            self.end = self.begin
        else:
            dlln = DoubleLinkedListNode(obj, self.end, None)
            self.end.next = dlln
            self.end = dlln
        self.elements += 1

    def pop(self):
        """Removes the last item and returns it."""
        node = self.end
        if node is None:
            return
        self.end = node.prev
        if node.prev is None:
            self.end = None
            self.begin = self.end
        else:
            node.prev.next = None
        self.elements -= 1
        return node.value

    def shift(self, obj):
        """Another name for push."""
        if self.begin is None:
            dlln = DoubleLinkedListNode(obj, None, None)
            self.begin = dlln
            self.end = self.begin
        else:
            dlln = DoubleLinkedListNode(obj, None, self.begin)
            self.begin.prev = dlln
            self.begin = dlln
        self.elements += 1

    def unshift(self):
        """Remove the first item and returns it."""
        node = self.begin
        if node is None:
            return
        self.begin = self.begin.next
        if self.begin is None:
            self.end = None
        else:
            self.begin.prev = None
        self.elements -= 1
        return node.value

    def remove(self, obj):
        """Find a matching item and removes it from the list."""
        indx = 0
        node = self.begin
        if node is None:
            return
        dlln = DoubleLinkedListNode(obj, None, None)
        if node.value == dlln.value:
            self.unshift()
        else:
            indx += 1
            while node.next.value != dlln.value:
                indx += 1
                node = node.next
                if node.next is None:
                    return
            node.next = node.next.next
            if node.next is None:
                # last node
                self.end = node
            else:
                node.next.next.prev = node.value
            self.elements -= 1
        return indx

    def first(self):
        """Return a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Return a *reference* to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        return self.elements

    def get(self, index):
        """Get the value at index."""
        count = 0
        node = self.begin
        while count < index:
            count += 1
            node = node.next
        return node and node.value

    def get_node(self, index):
        """Get the node at index."""
        count = 0
        node = self.begin
        while count < index:
            count += 1
            node = node.next
        return node

    def __repr__(self):
        string = 'ɸ '
        init = self.begin
        while init:
            string += f'<- {init.value} ->'
            init = init.next
        string += ' ɸ'
        return string
