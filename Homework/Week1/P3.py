#Problem 3
n = int(input("Enter the number: "))

def formlist(n):    #This fuction takes the number n, splits it into seperate digits and forms a sorted list comprised of those digits
    l = []
    while n != 0:
        x = n% 10
        l.append(x)
        n = int(n / 10)
    l.sort()
    return l

def formnumber(x):    #This function forms the number equivalend to the digits in the list but before that it checks that the number meets certain conditions
    if x < 0:
        x = x*(-1)
        negative = True
    else:
        negative = False
    a = formlist(x)
    if negative:
        a.reverse()
    s = 0
    for i in range(0, len(a)):
        s = s*10 + a[i]

    if negative:
        return s*(-1)
    else:
        return s

a = formnumber(n)
print(a)












































