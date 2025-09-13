from queues import Queue


def test_push():
    colors = Queue()
    colors.shift('Pthalo Blue')
    assert colors.count() == 1
    colors.shift('Ultramarine Blue')
    assert colors.count() == 2
    colors.shift('Cyan Blue')
    assert colors.count() == 3
    colors.shift('Red')
    assert colors.count() == 4


def test_unshift():
    colors = Queue()
    colors.shift('Viridian')
    colors.shift('Sap Green')
    colors.shift('Yellow')
    colors.shift('Van Dyke')
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


def test_first():
    colors = Queue()
    colors.shift('Cadmium Red Light')
    assert colors.first() == 'Cadmium Red Light'
    colors.shift('Hansa Yellow')
    assert colors.first() == 'Cadmium Red Light'
    colors.shift('Pthalo Green')
    assert colors.first() == 'Cadmium Red Light'
    colors.shift('Deb Orange')
    assert colors.first() == 'Cadmium Red Light'
    colors.shift('Blue Sky')
    assert colors.unshift() == 'Cadmium Red Light'
    assert colors.first() == 'Hansa Yellow'
