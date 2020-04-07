'''
Created on Oct 29, 2018

@author: Adi

This module contains all the UI functions
'''

from operations import parse_string

def showmenu():
    print("List of commands: ")
    print("add <sum> <category>")
    print("insert <day> <sum> <category>")
    print("remove <day> | <start day> to <end day> | <category>")
    
def main():
    showmenu()
    expenses = []
    #init_list(expenses)

    while True:
        n = input(">")
        if n == 'exit':
            return

        parse_string(expenses, n)

        
