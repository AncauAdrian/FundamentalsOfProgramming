def create(_day, _sum, _category):
    entry = {'day': _day, 'sum': _sum, 'category': _category}
    return entry


def add_new_entry(expenses, _day, _sum, _category):
    new = create(_day, _sum, _category)
    expenses.append(new)


def get_day(i):
    return i['day']


def get_value(i):
    return i['sum']


def get_category(i):
    return i['category']
