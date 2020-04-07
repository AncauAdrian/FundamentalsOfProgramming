from  math import sqrt

def strtoint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
    
def create_complex_number(x, y):
    try:
        a = strtoint(x)
        b = strtoint(y)
        #d = {"re" : a, "im" : b}    # For dictionaries
        d = (a, b)                 # For tuples
    except:
        return
    
    return d
    

def format_individual_number(a):
    """
    This numbers takes the string a and then formats it into a dictionary containing the imaginary and real part of the imaginary number
    """
    
    a.strip()
    
    if a.endswith('i'):
        d = create_complex_number('0', a[0:len(a) - 1])
    else:
        d = create_complex_number(a, '0')

    if d != None:
        return d
    
    if len(a) <= 1:
        return
    i = 0
    if a[0] == '+' or a[0] == '-':
        i = 1
    else: i = 0

    while a[i] != '+' and a[i] != '-' and i < len(a) - 1:
        i += 1

    x = a[0:i]
    y = a[i:len(a)]

    if x[len(x) - 1] != 'i' and y[len(y) - 1] != 'i':
        return

    if y[len(y) - 1] != 'i' and x.endswith('i'):
        x,y = y, x

    y = y[0:len(y) - 1]

    d = create_complex_number(x, y)
    if d == None:
        return
    
    return d

def get_re_part(x):
    #return x['re']  # For dictionaries
    return x[0]    # For tuples
            
def get_im_part(x):
    #return x['im']  # For dictionaries
    return x[1]    # For tuples

def get_modulus(x):
    """
    Gets the modulus of complex number x
    """
    return sqrt(get_re_part(x) * get_re_part(x) + get_im_part(x) * get_im_part(x))

def assert_modulus():
    c = { 'im' : -4, 're' : 3 }
    assert get_modulus(c) == 5

def get_seq_modulus(x):
    """
    This functions goes through all the numbers in x and finds the longest sequence that has the same modulus
    """
    i = 1
    start = 0
    end = 0
    curlen = 1
    maxlen = 1

    while i <= len(x):
        if i == len(x):
            if curlen > maxlen:
                end = i
                start = i - curlen
                maxlen = curlen
        else:   
            if get_modulus(x[i - 1]) == get_modulus(x[i]):
                curlen += 1
                    
            else:      
                if curlen > maxlen:
                    end = i
                    start = i - curlen
                    maxlen = curlen

                curlen = 1
        i += 1

    if maxlen == 1:
        return None
    else:
        return x[start:end]

def get_real_distinct(x):
    """
    This functions returns the longest sequence in x of numbers that are real
    """
    i = 1
    start = 0
    end = 0
    curlen = 1
    maxlen = 1

    while i <= len(x):
        if i == len(x):
            if curlen > maxlen:
                end = i
                start = i - curlen
                maxlen = curlen
        else:
            if get_im_part(x[i - 1]) == 0 and get_im_part(x[i]) == 0:
                curlen += 1
            else:                  
                if curlen > maxlen:
                    end = i
                    start = i - curlen
                    maxlen = curlen

                curlen = 1
        i += 1

    if maxlen == 1:
        return None
    else:
        return x[start:end]


def readcomplexnumbers(x):
    """
    Reads a series of complex numbers and then puts them in a list
    """
    i = 0
    print("Reading list, enter values below: (just press enter/type nothing to stop")
    while True:
        a = str(input())
        if a == '':
            break
        dic = format_individual_number(a)
        
        if dic == None:
            print("Invalid number! Complex number must be entered under the format: a+bi (no spaces if possible)")
            continue

        print()
        x.append(dic)

    return x
        
def printnumber(i):
    if get_im_part(i) > 0:
        print(str(get_re_part(i)) + "+" + str(get_im_part(i)) + "i")
    elif get_im_part(i) == 0:
         print(str(get_re_part(i)) + "+" + str(get_im_part(i)) + "i")
    else:
        print(str(get_re_part(i)) + str(get_im_part(i)) + "i")

def printlist(x):
    print("List: ")
    for i in x:
        printnumber(i)
    
def showmenu():
    print("\nCommands: ")
    print("1 - to read a list of complex numbers")
    print("2 - to print the list of numbers")
    print("3 - to print to console the longest sequence in the list in which the numbers have the same module (3)")
    print("4 - to print to console the longest sequence that contains real numbers (5)")
    print("5 - to clear the list")
    print("0 - to exit the program")

def init(x):
    x = [(3, 4), (-3, 4), (3, -4), (-90, 0), (66, 0), (-3, 0), (7, 0), (333, 4), (3, -64), (23, 0), (35, 0)]
    return x

def main():
    listt = []
    listt = init(listt)
    showmenu()
    while True:

        n = int(input("\nEnter command: "))

        if n == 0: break
        if n == 1:
            listt = readcomplexnumbers(listt)
        elif n == 2:
                printlist(listt)
        elif n == 3:
            seq = get_seq_modulus(listt)
            if seq == None:
                print("There is no sequence with a length greater than 1 that has that property")
            else:
                printlist(seq)
        elif n == 4:
            seq = get_real_distinct(listt)
            if seq == None:
                print("There is no sequence with a length greater than 1 that has that property")
            else:
                printlist(seq)
        elif n == 5:
            listt = []
            print("List cleared!")
        else:
            print("Invalid Command!")
            pass


main()
        
    




