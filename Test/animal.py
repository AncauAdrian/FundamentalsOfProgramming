def create_animal(code, name, _type, species):
    return {'code': code, 'name': name, 'type': _type, 'species': species}


def get_code(animal):
    return animal['code']


def get_name(animal):
    return animal['name']


def get_type(animal):
    return animal['type']


def get_species(animal):
    return animal['species']


def set_type(animal, new_type):
    animal['type'] = new_type


def test_create_animal():
    c = create_animal('Z01', 'Alex', 'herbivore', 'zebra')

    assert get_code(c) == 'Z01'
    assert get_name(c) == 'Alex'
    assert get_type(c) == 'herbivore'
    assert get_species(c) == 'zebra'


test_create_animal()