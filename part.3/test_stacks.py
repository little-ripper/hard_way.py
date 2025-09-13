from stacks import Stack


def test_push():
    colors = Stack()
    colors.push('Pthalo Blue')
    assert colors.count() == 1
    colors.push('Ultramarine Blue')
    assert colors.count() == 2
    colors.push('Cyan Blue')
    assert colors.count() == 3
    colors.push('Red')
    assert colors.count() == 4


def test_pop():
    colors = Stack()
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


def test_topper():
    colors = Stack()
    colors.push('Cadmium Red Light')
    assert colors.topper() == 'Cadmium Red Light'
    colors.push('Hansa Yellow')
    assert colors.topper() == 'Hansa Yellow'
    colors.push('Pthalo Green')
    assert colors.topper() == 'Pthalo Green'
    colors.push('Deb Orange')
    assert colors.topper() == 'Deb Orange'
    colors.push('Blue Sky')
    assert colors.topper() == 'Blue Sky'
    assert colors.pop() == 'Blue Sky'
    assert colors.topper() == 'Deb Orange'
