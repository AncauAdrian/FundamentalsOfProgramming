'''
Created on Oct 29, 2018

@author: Adi

This module contains operations on tables and others
'''

def strtoint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
    
    
def parse_string(expenses, string):
    pass