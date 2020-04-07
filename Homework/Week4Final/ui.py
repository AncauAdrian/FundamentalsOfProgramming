from operations import parse_string, init_list, colorString
from domain import *


def print_list(_list):
    for i in _list:
        print("Day - " + str(get_day(i)) + " >>> Amount - " + str(get_value(i)) + " >>> Category - " + str(
            get_category(i)))


def showmenu():
    print("List of commands: ")
    print(colorString("list"))
    print(colorString("list") + " <category>")
    print(colorString("list") + " <category> [ < | = | > ] <value>")
    print(colorString("add") + " <sum> <category>")
    print(colorString("insert") + " <day> <sum> <category>")
    print(colorString("remove") + " <day> | <start day> " + colorString("to") + " <end day> | <category>")
    print(colorString("sum") + " <category>")
    print(colorString("max") + " <day>")
    print(colorString("sort") + " <day> | <category>")
    print(colorString("filter") + " <category>")
    print(colorString("filter") + " <category> [ < | = | > ] <value>")

def main():
    showmenu()
    expenses = []
    undo = []
    init_list(expenses)

    while True:
        n = input(colorString(">"))
        if n == 'exit':
            return
        if n == 'help':
            showmenu()
        elif n == 'undo':
            if len(undo) == 0:
                print("Nothing to undo")
            else:
                undo.pop()
                expenses = undo[-1]
        else:
            try:
                ret = parse_string(expenses, n, undo)
                if ret is not None:
                    try:
                        print_list(ret)
                    except:
                        print(ret)
            except Exception as e:
                print(e)
