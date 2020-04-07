#By researching the topic of perfect numbers we find out that a theory exists (the Euclid-Euler theory), that defines a formula for finding perfect numbers: if 2^p - 1 is prime then 2^(p − 1)(2^p − 1) is a Perfect Number

n = int(input("Enter a number: "))

def isprime(x):     #Checks whether the number x is prime and returns a boolean value accordingly
    if x == 1:
        return False
    if x == 2:
        return True

    i = 2
    while i*i < x:
        if x % i == 0:
            return False
        else:
            i = i + 1

    return True

def find_prfnbr(x):
    if x < 6:
        return 6
    
    power = 4
    while isprime(power - 1) == False or (power - 1)*power/2 <= x:
        power = power * 2

    return (power - 1)*power/2

print(find_prfnbr(n))
