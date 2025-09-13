# -*- mode:python-ts; -*-
# car-0 { value: 10,
#         nxt: car-1 { value: 20,
#                      nxt: car-2 { value: 30,
#                                   nxt; car-3 { value: 40,
#                                                nxt: None }}}}
class SingleLinkedListNode:
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        nval = self.nxt and self.nxt.value or None
        return f'[{self.value} -> {repr(nval)}]'


# Controller - Network
class SingleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self.elements = 0

    def push(self, obj):
        """Append a new value on the end of the list."""
        slln = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = slln
            self.end = self.begin
        else:
            self.end.nxt = slln
            self.end = slln
        self.elements += 1

    def pop(self):
        """Removes the last item and returns it."""
        node = self.begin
        if node is None:
            return
        elif node.nxt is None:
            name = self.begin.value
            self.begin = None
            self.end = self.begin
            self.elements -= 1
            return name
        else:
            while node.nxt.value != self.end.value:
                node = node.nxt
            name = self.end.value
            self.end = node
            self.end.nxt = None
            self.elements -= 1
            return name

    def shift(self, obj):
        """Another name for push?? Not really!!
        Shift push from the other side!"""
        if self.begin is None:
            slln = SingleLinkedListNode(obj, None)
            self.begin = slln
            self.end = self.begin
        else:
            slln = SingleLinkedListNode(obj, self.begin)
            self.begin = slln
        self.elements += 1

    def unshift(self):
        """Remove the first item and returns it."""
        node = self.begin
        if node is None:
            return
        self.begin = self.begin.nxt
        if self.begin is None:
            self.end = None
        self.elements -= 1
        return node.value

    def remove(self, obj):
        """Find a matching item and removes it from the list."""
        indx = 0
        node = self.begin
        if node is None:
            return
        slln = SingleLinkedListNode(obj, None)
        if node.value == slln.value:
            self.unshift()
        else:
            indx += 1
            while node.nxt.value != slln.value:
                indx += 1
                node = node.nxt
                if node.nxt is None:
                    return
            node.nxt = node.nxt.nxt
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
            node = node.nxt
        return node and node.value

    def __repr__(self):
        string = ''
        init = self.begin
        while init:
            string += f'{init.value} -> '
            init = init.nxt
        string += 'ɸ'
        return string
