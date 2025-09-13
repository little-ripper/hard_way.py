from double_linked_lists import DoubleLinkedList


def test_push():
    colors = DoubleLinkedList()
    colors.push('Pthalo Blue')
    assert colors.count() == 1
    colors.push('Ultramarine Blue')
    assert colors.count() == 2
    colors.push('Cyan Blue')
    assert colors.count() == 3
    colors.push('Red')
    assert colors.count() == 4


def test_pop():
    colors = DoubleLinkedList()
    colors.push('Magenta')
    colors.push('Green')
    colors.push('Yellow')
    colors.push('Alizarin')
    assert colors.count() == 4
    assert colors.pop() == 'Alizarin'
    assert colors.count() == 3
    assert colors.pop() == 'Yellow'
    assert colors.count() == 2
    assert colors.pop() == 'Green'
    assert colors.count() == 1
    assert colors.pop() == 'Magenta'
    assert colors.count() == 0
    assert colors.pop() is None
    assert colors.count() == 0
    assert colors.count() == 0


def test_shift():
    colors = DoubleLinkedList()
    colors.shift('Cadmium Orange')
    assert colors.count() == 1
    colors.shift('Carbazole Violet')
    assert colors.count() == 2
    assert colors.pop() == 'Cadmium Orange'
    assert colors.count() == 1
    assert colors.pop() == 'Carbazole Violet'
    assert colors.count() == 0


def test_unshift():
    colors = DoubleLinkedList()
    colors.push('Viridian')
    colors.push('Sap Green')
    colors.push('Yellow')
    colors.push('Van Dyke')
    assert colors.count() == 4
    assert colors.unshift() == 'Viridian'
    assert colors.count() == 3
    assert colors.unshift() == 'Sap Green'
    assert colors.count() == 2
    assert colors.unshift() == 'Yellow'
    assert colors.count() == 1
    assert colors.unshift() == 'Van Dyke'
    assert colors.count() == 0
    assert colors.unshift() is None
    assert colors.count() == 0
    assert colors.count() == 0
