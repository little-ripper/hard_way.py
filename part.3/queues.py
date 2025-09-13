class QueueNode:
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f'[{repr(pval)} <- {self.value} -> {repr(nval)}]'


class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.elements = 0

    def shift(self, obj):
        """Pushes a new value to the top of the queue."""
        if self.top is None:
            qn = QueueNode(obj, None, None)
            self.top = qn
            self.bottom = self.top
        else:
            qn = QueueNode(obj, None, self.top)
            self.top.prev = qn
            self.top = qn
        self.elements += 1

    def unshift(self):
        """Remove the first item inserted and returns it."""
        node = self.bottom
        if node is None:
            return
        self.bottom = node.prev
        if node.prev is None:
            self.bottom = None
            self.top = self.bottom
        else:
            node.prev.next = None
        self.elements -= 1
        return node.value

    def count(self):
        return self.elements

    def first(self):
        """Return a *reference* to the first item that can go out,
        does not remove."""
        return self.bottom.value

    def __repr__(self):
        string = '->'
        init = self.top
        while init:
            string += f'|<- {init.value} ->|'
            init = init.next
        string += '<-'
        return string
