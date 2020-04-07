from animal import *


def add_animal(animal_list, code, name, _type, species):
    """
    This function takes the parameters code, name, _type and species, it creates an animal with those values (dictionary)
    and adds that animal to the animal_list.
    It also checks whether one of the parameters is void or the code entered is already in used and raises an error
    accordingly.
    """
    if code == '' or name == '' or _type == '' or species == '':
        raise ValueError("[ERROR] One or more of the fields is void")

    for i in animal_list:
        if get_code(i) == code:
            raise ValueError("[ERROR] The code is already used")

    animal_list.append(create_animal(code, name, _type, species))


def modify_type(animal_list, code, new_type):
    """
    This function finds the animal in animal_list that has the given code and modifies its type with its new_type value.
    If the animal with the specified code doesn't exist it raises an error accordingly.
    """
    for i in animal_list:
        if get_code(i) == code:
            set_type(i, new_type)
            return

    raise ValueError("[ERROR] The animal with the specified code does not exist")


def modify_all_types(animal_list, species, new_type):
    if new_type == '':
        raise ValueError("[ERROR] The new type must not be void")

    for i in animal_list:
        if get_species(i) == species:
            set_type(i, new_type)

    return


def sort_list(animal_list):
    new_list = animal_list[:]

    for i in range(len(new_list) - 1):
        for j in range(i + 1, len(new_list)):
            if get_name(new_list[j]) < get_name(new_list[i]):
                cache = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = cache

    return new_list


def test_operations():
    _list = []
    add_animal(_list, 'Z01', 'Alex', 'herbivore', 'zebra')
    assert get_code(_list[0]) == 'Z01'
    assert get_name(_list[0]) == 'Alex'
    assert get_type(_list[0]) == 'herbivore'
    assert get_species(_list[0]) == 'zebra'

    add_animal(_list, 'L01', 'Kevin', 'carnivore', 'lion')

    assert get_code(_list[1]) == 'L01'
    assert get_name(_list[1]) == 'Kevin'
    assert get_type(_list[1]) == 'carnivore'
    assert get_species(_list[1]) == 'lion'

    try:
        add_animal(_list, 'Z01', 'Alex', 'herbivore', 'zebra')
        assert False
    except ValueError as e:
        assert True

    assert get_code(_list[0]) == 'Z01'
    assert get_name(_list[0]) == 'Alex'
    assert get_type(_list[0]) == 'herbivore'
    assert get_species(_list[0]) == 'zebra'

    try:
        add_animal(_list, 'Z02', '', '', '')
        assert False
    except ValueError as e:
        assert True

    modify_type(_list, 'Z01', 'omnivore')
    assert get_type(_list[0]) == 'omnivore'

    new = sort_list(_list)
    assert new == _list


test_operations()
