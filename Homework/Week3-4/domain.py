'''
Created on Oct 29, 2018

@author: Adi

This module contains the function that creates the table, getters, setters and so on...
'''

def add_new_entry(expenses, _day, _sum, _category):
    entry = {'day' : _day, 'sum' : _sum, 'category' : _category}
    expenses.append(entry)
    
def get_day(i):
    return i['day']

def get_sum(i):
    return i['sum']

def get_category(i):
    return i['category']
