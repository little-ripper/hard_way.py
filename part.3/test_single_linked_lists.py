from single_linked_lists import SingleLinkedList


def test_push():
    colors = SingleLinkedList()
    colors.push('Pthalo Blue')
    assert colors.count() == 1
    colors.push('Ultramarine Blue')
    assert colors.count() == 2
    colors.push('Cyan Blue')
    assert colors.count() == 3
    colors.push('Red')
    assert colors.count() == 4


def test_pop():
    colors = SingleLinkedList()
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
    colors = SingleLinkedList()
    colors.shift('Cadmium Orange')
    assert colors.count() == 1
    colors.shift('Carbazole Violet')
    assert colors.count() == 2
    assert colors.pop() == 'Cadmium Orange'
    assert colors.count() == 1
    assert colors.pop() == 'Carbazole Violet'
    assert colors.count() == 0


def test_unshift():
    colors = SingleLinkedList()
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


def test_remove():
    colors = SingleLinkedList()
    colors.push('Cobalt')
    colors.push('Zinc White')
    colors.push('Nickle Yellow')
    colors.push('Perinone')
    assert colors.remove('Cobalt') == 0
    assert colors.remove('DONT EXIST') is None
    assert colors.remove('Perinone') == 2
    assert colors.remove('Nickle Yellow') == 1
    assert colors.remove('Zinc White') == 0
    assert colors.remove('NO ITEMS ANYMORE') is None


def test_first():
    colors = SingleLinkedList()
    colors.push('Cadmium Red Light')
    assert colors.first() == 'Cadmium Red Light'
    colors.push('Hansa Yellow')
    assert colors.first() == 'Cadmium Red Light'
    colors.push('Pthalo Green')
    assert colors.first() == 'Cadmium Red Light'
    colors.shift('Deb Orange')
    assert colors.first() == 'Deb Orange'
    colors.shift('Blue Sky')
    assert colors.first() == 'Blue Sky'


def test_last():
    colors = SingleLinkedList()
    colors.push('Cadmium Red Light')
    assert colors.last() == 'Cadmium Red Light'
    colors.push('Hansa Yellow')
    assert colors.last() == 'Hansa Yellow'
    colors.shift('Pthalo Green')
    assert colors.last() == 'Hansa Yellow'


def test_get():
    colors = SingleLinkedList()
    colors.push('Vermillion')
    assert colors.get(0) == 'Vermillion'
    colors.push('Sap Green')
    assert colors.get(0) == 'Vermillion'
    assert colors.get(1) == 'Sap Green'
    colors.push('Cadmium Yellow Light')
    assert colors.get(0) == 'Vermillion'
    assert colors.get(1) == 'Sap Green'
    assert colors.get(2) == 'Cadmium Yellow Light'
    assert colors.pop() == 'Cadmium Yellow Light'
    assert colors.get(0) == 'Vermillion'
    assert colors.get(1) == 'Sap Green'
    assert colors.get(2) is None
    colors.pop()
    assert colors.get(0) == 'Vermillion'
    colors.pop()
    assert colors.get(0) is None
