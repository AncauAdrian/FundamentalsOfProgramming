import unittest
from domain.Student import Student


class Structure:
    def __init__(self, _list=None):
        if _list is None:
            self._list = list()
        else:
            self._list = _list
        self._index = 0

    def __iter__(self):
        """if hasattr(self._list[0], "__iter__"):
            return self._list[0].__iter__()
        return self._list.__iter__()"""

        return self._list.__iter__()

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __delitem__(self, key):
        del self._list[key]

    def __next__(self):
        if not self._list:
            raise StopIteration
        elif self._index == len(self._list) - 1:
            raise StopIteration
        else:
            self._index += 1
        return self._list[self._index]

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return repr(self._list)

    def append(self, other):   # append ?
        self._list.append(other)


def insertion_sort(array, comp_greater):
    if len(array) == 1 or len(array) == 0:
        return array

    i = 1
    while i < len(array):
        j = i
        while j > 0 and comp_greater(array[j - 1], array[j]):       # >
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1

    return array


def filter_array(array, filter_function):
    new = list()

    for i in array:
        if filter_function(i):
            new.append(i)

    return new


class Test(unittest.TestCase):
    def test_iterations(self):
        self._list = [1, 2, 3, 4, 5]
        self._struct = Structure(self._list)

        self.assertEqual(len(self._struct), len(self._list))
        self.assertEqual(self._struct[0], self._list[0])
        #self.assertEqual(self._struct, self._list) ????????????????????

        self.assertEqual(next(self._struct), 2)
        self.assertEqual(next(self._struct), 3)
        self.assertEqual(next(self._struct), 4)
        self.assertEqual(next(self._struct), 5)
        self.assertRaises(StopIteration, next, self._struct)

        del self._struct[0]

        self.assertEqual(self._struct[0], 2)
        self.assertEqual(len(self._struct), len(self._list))

        self.assertIn(5, self._struct)

        if 6 not in self._struct:
            assert True

        for i in self._struct:
            print(i)

        self._struct = Structure([Student(1, 'Test'), Student(2, 'Test2')])

        if Student(1, 'T') not in self._struct:
            assert False

    def test_insertion_sort(self):
        l = [6, 2, 3, 1, 0, 5, 4]
        insertion_sort(l, lambda x, y: x > y)
        self.assertEqual(l, [0, 1, 2, 3, 4, 5, 6])

    def test_filter_array(self):
        l = [0, 1, 2, 3, 4, 5, 6]
        new = filter_array(l, lambda x: x % 2 == 0)
        self.assertEqual(new, [0, 2, 4, 6])