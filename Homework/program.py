import datetime

def strtoint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def add_new_entry(expenses, _day, _sum, _category):
    entry = {'day' : _day, 'sum' : _sum, 'category' : _category}
    expenses.append(entry)

def get_day(i):
    return i['day']

def get_sum(i):
    return i['sum']

def get_category(i):
    return i['category']

def parse_string(expenses, string):
    if len(string) == 0:
        print("[ERROR] Invalid command!")
        return
    
    expenses[:]
    cache = string.split()
    cmd = cache[0]
    params = cache[1:]
    listofcmds = {"add" : add, "insert": insert, "remove": remove, 'list' : _list}

    if cmd not in listofcmds.keys():
        print("[ERROR] Invalid command!")
        return

    listofcmds[cmd](expenses, params)

def _list(expenses, params):
    cat_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']
    comp_params = {'<' : cmpr_smaller , '=' : cmpr_equal, '>' : cmpr_greater}
    if len(params) == 0:
        print_list(expenses)
    elif len(params) == 1:
        cat = params[0]
        if cat in cat_params:
            l = get_list_category(expenses, cat)
            print_list(l)
        else:
            print("[ERROR] Invalid parameter in command [list]")
            return
            
    elif len(params) == 3:
        cat = params[0]
        comp = params[1]
        if cat not in cat_params:
            print("[ERROR] Invalid parameters in command [list]")
            return

        if comp not in comp_params.keys():
            print("[ERROR] Invalid parameters in command [list]")
            return
        
        try:
            num = strtoint(params[2])
        except:
            print("[ERROR] Invalid parameters in command [list]")
            return

        l = get_list_bounded(expenses, cat, comp, num)
        print_list(l)
        
    else:
        print("[ERROR] Invalid parameters in command [list]")
        return

def print_list(_list):
    for i in _list:
        print("Day - " + str(get_day(i)) + " >>> Ammount - " + str(get_sum(i)) + " >>> Category - " + str(get_category(i)))

def get_list_category(expenses, cat):
    new = []
    for i in expenses:
        if get_category(i) == cat:
            new.append(i)

    return new

def get_list_bounded(expenses, cat, comp, num):
    new = []
    comp_params = {'<' : cmpr_smaller , '=' : cmpr_equal, '>' : cmpr_greater}
    for i in expenses:
        if get_category(i) == cat and comp_params[comp](i, num):
            new.append(i)

    return new
        
    
def cmpr_equal(i, n):
    if get_sum(i) == n:
        return True

    return False

def cmpr_smaller(i, n):
    if get_sum(i) < n:
        return True

    return False

def cmpr_greater(i, n):
    if get_sum(i) > n:
        return True

    return False


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
                print("[ERROR] Invalid parameters in command [remove]")
                return
            
            remove_items_by_day(expenses, par)

    elif len(params) == 3 and params[1] == 'to':
        try:
            first = strtoint(params[0])
            second = strtoint(params[2])

            if first >= second:
                raise

            if first < 1 or first > 31 or second < 1 or second > 31:
                raise
        except:
            print("[ERROR] Invalid parameters in command [remove]")
            return
    
        remove_items_by_interval(expenses, first, second)
    else:
        print("[ERROR] Invalid parameters in command [remove]")
        return

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

    if len(params) != 2:
        print("[ERROR] Invalid parameters in command [add]!")
        return

    try:
        x = strtoint(params[0])
    except:
       print("[ERROR] Invalid input for first parameter <sum> in command [add]! - Parameter not numerical")

    if params[1] not in second_params:
        print("[ERROR] Invalid input for second parameter <category> in command [add]!")
        return
    cat = params[1]
    
    now = datetime.datetime.now()

    add_new_entry(expenses, now.day, x, cat)

def insert(expenses, params):
    second_params = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']

    if len(params) != 3:
        print("[ERROR] Invalid parameters in command [insert]!")
        return

    try:
        date = strtoint(params[0])
        if date < 1 or date > 31:
            raise

        if type(date) is not int:
            raise
        
    except:
       print("[ERROR] Invalid input for first parameter <date> in command [insert]! - Parameter not numerical or a natural number between >= 1 and <=31")

    try:
        x = strtoint(params[1])
    except:
       print("[ERROR] Invalid input for second parameter <sum> in command [insert]! - Parameter not numerical")

    if params[2] not in second_params:
        print("[ERROR] Invalid input for third parameter <category> in command [insert]!")
        return

    cat = params[2]

    add_new_entry(expenses, date, x, cat) 
    

def showmenu():
    print("List of commands: ")
    print("add <sum> <category>")
    print("insert <day> <sum> <category>")
    print("remove <day> | <start day> to <end day> | <category>")


def init_list(a):
    add_new_entry(a, 20, 95, "housekeeping")
    add_new_entry(a, 20, 66, "food")
    add_new_entry(a, 15, 9, "food")
    add_new_entry(a, 22, 33, "others")
    add_new_entry(a, 2, 267, "internet")
    add_new_entry(a, 30, 48, "others")
    add_new_entry(a, 13, 12, "transport")
    add_new_entry(a, 6, 100, "clothin")
    add_new_entry(a, 19, 55, "others")
    add_new_entry(a, 19, 28, "clothing")

def main():
    showmenu()
    expenses = []
    init_list(expenses)

    while True:
        n = input(">")
        if n == 'exit':
            return

        parse_string(expenses, n)

        

main()
