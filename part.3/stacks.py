class StackNode:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f'[{self.value} -> {repr(nval)}]'


class Stack:
    def __init__(self):
        self.top = None
        self.elements = 0

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        sn = StackNode(obj, self.top)
        self.top = sn
        self.elements += 1

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        node = self.top
        if node is None:
            return
        self.top = node.next
        self.elements -= 1
        return node.value

    def topper(self):
        """Return a *reference* to the first item, does not remove."""
        return self.top.value

    def count(self):
        return self.elements

    def __repr__(self):
        string = '->'
        init = self.top
        while init:
            string += f' {init.value} |'
            init = init.next
        return string
