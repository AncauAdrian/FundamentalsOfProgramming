from domain import *
from copy import deepcopy
import datetime

def colorString(string):
    #cred = '\033[91m'
    #cend = '\033[0m'
    #return cred + string + cend
    return string

def strtoint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def cmpr_equal(i, n):
    if i == n:
        return True
    return False


def cmpr_smaller(i, n):
    if i < n:
        return True

    return False


def cmpr_greater(i, n):
    if i > n:
        return True

    return False


def set_list_category(expenses, cat):
    i = 0
    j = len(expenses)
    while i < j:
        if get_category(expenses[i]) != cat:
            del expenses[i]
            j -= 1
        else:
            i += 1


def get_list_category(expenses, cat):
    new = []
    for i in expenses:
        if get_category(i) == cat:
            new.append(i)

    return new


def set_list_bounded(expenses, cat, comp, num):
    comp_params = {'<': cmpr_smaller, '=': cmpr_equal, '>': cmpr_greater}
    i = 0
    j = len(expenses)
    while i < j:
        if get_category(expenses[i]) == cat and comp_params[comp](get_value(expenses[i]), num) is True:
            i += 1
        else:
            del expenses[i]
            j -= 1


def get_list_bounded(expenses, cat, comp, num):
    new = []
    comp_params = {'<': cmpr_smaller, '=': cmpr_equal, '>': cmpr_greater}
    for i in expenses:
        if get_category(i) == cat and comp_params[comp](get_value(i), num):
            new.append(i)

    return new


def parse_string(expenses, string, undo):
    if len(string) == 0:
        raise Exception(colorString("[ERROR]") + " Invalid command!")

    expenses[:]
    undo[:]
    if len(undo) == 0:
        undo.append(deepcopy(expenses))

    if len(undo) > 0 and expenses != undo[len(undo) - 1]:
        undo.append(deepcopy(expenses))

    cache = string.split()
    cmd = cache[0]
    params = cache[1:]
    listofcmds = {"add": add, "insert": insert, "remove": remove, 'list': _list, 'sum': _sum, 'max': _max,
                  'sort': _sort, 'filter': _filter}

    if cmd not in listofcmds.keys():
        raise Exception(colorString(colorString("[ERROR]") + "") + " Invalid command!")
    try:
        return listofcmds[cmd](expenses, params)
    except Exception as e:
        raise Exception(e)


def _filter(expenses, params):
    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    comp_params = {'<': cmpr_smaller, '=': cmpr_equal, '>': cmpr_greater}
    new = []

    if len(params) == 0:
        raise Exception(colorString("[ERROR]") + " Invalid parameter in command [filter]")
    elif len(params) == 1:
        cat = params[0]
        if cat in cat_params:
            set_list_category(expenses, cat)
        else:
            raise Exception(colorString("[ERROR]") + " Invalid parameter in command [filter]")
    elif len(params) == 3:
        cat = params[0]
        comp = params[1]
        if cat not in cat_params:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [filter]")

        if comp not in comp_params.keys():
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [filter]")

        try:
            num = strtoint(params[2])
        except:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [filter]")

        set_list_bounded(expenses, cat, comp, num)
    else:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [filter]")

def _list(expenses, params):
    expenses[:]
    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    comp_params = {'<': cmpr_smaller, '=': cmpr_equal, '>': cmpr_greater}
    if len(params) == 0:
        return expenses
    elif len(params) == 1:
        cat = params[0]
        if cat in cat_params:
            return get_list_category(expenses, cat)
        else:
            raise Exception(colorString("[ERROR]") + " Invalid parameter in command [list]")

    elif len(params) == 3:
        cat = params[0]
        comp = params[1]
        if cat not in cat_params:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [list]")

        if comp not in comp_params.keys():
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [list]")

        try:
            num = strtoint(params[2])
        except:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [list]")

        return get_list_bounded(expenses, cat, comp, num)
    else:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [list]")


def _sort(expenses, params):
    if len(params) != 1:
        raise Exception(colorString("[ERROR]") + " Invalid parameter in command [sort]")
    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']

    par = params[0]
    if par in cat_params:
        return sort_items_cat(expenses, par)
    else:
        try:
            par = strtoint(params[0])
        except:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [sort]")

        return sort_items_day(expenses, par)


def sort_items_cat(expenses, cat):
    sorted_list = []
    for i in expenses:
        if get_category(i) == cat:
            new = create(get_day(i), get_value(i), get_category(i))
            sorted_list.append(new)

    newlist = sorted(sorted_list, key=lambda k: get_value(k))
    return newlist


def sort_items_day(expenses, day):
    sorted_list = []
    for i in expenses:
        if get_day(i) == day:
            new = create(get_day(i), get_value(i), get_category(i))
            sorted_list.append(new)

    newlist = sorted(sorted_list, key=lambda k: get_value(k))
    return newlist


def _max(expenses, params):
    if len(params) != 1:
        raise Exception(colorString("[ERROR]") + " Invalid parameter in command [max]")

    try:
        par = strtoint(params[0])
    except:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [max]")

    return get_max(expenses, par)


def get_max__(expenses):
    maxx = 0
    d = 0
    for i in range(1, 32):
        for j in expenses:
            if get_day(j) == i:
                s = get_day_sum(expenses, i)
                if s >= maxx:
                    maxx = s
                    d = i
    return d


def get_max(expenses, day):
    maxx = 0
    cat = 0
    val = 0

    for j in expenses:
        if get_day(j) == day:
            s = get_day_sum(expenses, day)
            if s >= maxx:
                maxx = s
                cat = get_category(j)
                val = get_value(j)

    new = []
    new.append(create(day, val, cat))
    #return "The day with the maximum expenses is >>> " + colorString(cat) + " >> " + str(val)
    return new


def get_day_sum(expenses, day):
    summ = 0
    for i in expenses:
        if get_day(i) == day:
            summ += get_value(i)

    return summ


def _sum(expenses, params):
    if len(params) != 1:
        raise Exception(colorString("[ERROR]") + " Invalid parameter in command [sum]")

    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    cat = params[0]
    if cat not in cat_params:
        raise Exception(colorString("[ERROR]") + " Invalid parameter in command [sum]")

    return str("The sum of all items of category " + colorString(cat) + " is >> " + str(_sum_cat(expenses, cat)))


def _sum_cat(expenses, cat):
    summ = 0
    for i in expenses:
        if get_category(i) == cat:
            summ += get_value(i)

    return summ


def remove(expenses, params):
    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    expenses[:]
    if len(params) == 1:
        par = params[0]
        if par in cat_params:
            remove_items_by_cat(expenses, par)
        else:
            try:
                par = strtoint(params[0])
            except:
                raise Exception(colorString("[ERROR]") + " Invalid parameters in command [remove]")

            remove_items_by_day(expenses, par)

    elif len(params) == 3 and params[1] == 'to':
        try:
            first = strtoint(params[0])
            second = strtoint(params[2])

            if first >= second:
                raise 0

            if first < 1 or first > 31 or second < 1 or second > 31:
                raise 0
        except:
            raise Exception(colorString("[ERROR]") + " Invalid parameters in command [remove]")

        remove_items_by_interval(expenses, first, second)
    else:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [remove]")


def remove_items_by_cat(expenses, cat):
    i = 0
    j = len(expenses)
    while i < j:
        if get_category(expenses[i]) == cat:
            del expenses[i]
            j -= 1
        else:
            i += 1


def remove_items_by_day(expenses, day):
    i = 0
    j = len(expenses)
    while i < j:
        if get_day(expenses[i]) == day:
            del expenses[i]
            j -= 1
        else:
            i += 1


def remove_items_by_interval(expenses, first, second):
    i = 0
    j = len(expenses)
    while i < j:
        if get_day(expenses[i]) >= first and get_day(expenses[i]) <= second:
            del expenses[i]
            j -= 1
        else:
            i += 1


def add(expenses, params):
    second_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    expenses[:]

    if len(params) != 2:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [add]!")

    try:
        x = strtoint(params[0])
    except:
        raise Exception(colorString("[ERROR]") + " Invalid input for first parameter <sum> in command [add]! - Parameter not numerical")

    if params[1] not in second_params:
        raise Exception(colorString("[ERROR]") + " Invalid input for second parameter <category> in command [add]!")

    cat = params[1]

    now = datetime.datetime.now()

    add_new_entry(expenses, now.day, x, cat)
    #return expenses


def insert(expenses, params):
    second_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    if len(params) != 3:
        raise Exception(colorString("[ERROR]") + " Invalid parameters in command [insert]!")

    try:
        date = strtoint(params[0])
        if date < 1 or date > 31:
            raise Exception(colorString("[ERROR]") + " Invalid date!")

        if type(date) is not int:
            raise Exception(colorString("[ERROR]") + " Invalid date!")

    except:
        raise Exception(colorString("[ERROR]") + " Invalid input for first parameter <date> in command [insert]! - Parameter not numerical or a natural number between >= 1 and <=31")

    try:
        x = strtoint(params[1])
    except:
        raise Exception(colorString("[ERROR]") + " Invalid input for second parameter <sum> in command [insert]! - Parameter not numerical")

    if params[2] not in second_params:
        raise Exception(colorString("[ERROR]") + " Invalid input for third parameter <category> in command [insert]!")

    cat = params[2]

    add_new_entry(expenses, date, x, cat)


def init_list(a):
    add_new_entry(a, 20, 95, "housekeeping")
    add_new_entry(a, 20, 66, "food")
    add_new_entry(a, 15, 9, "food")
    add_new_entry(a, 22, 33, "others")
    add_new_entry(a, 2, 267, "internet")
    add_new_entry(a, 30, 48, "others")
    add_new_entry(a, 13, 12, "transport")
    add_new_entry(a, 6, 100, "clothing")
    add_new_entry(a, 19, 55, "others")
    add_new_entry(a, 19, 28, "clothing")
