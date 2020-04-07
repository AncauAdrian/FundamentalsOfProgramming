n = int(input("Enter the number n: "))

def find_fibnumber(x):  #This function is going to generate the fibonacci sequence and return the smallest number m from that sequence that is also smaller than x and returns it and it's postion k in the sequence
    if x < 1:
        return 1, 0
    
    k = 2;
    a = 1
    b = 1

    while b <= n:
        cache = a + b
        a = b
        b = cache
        k = k + 1

    return b, k

m, pos = find_fibnumber(n)                  #Execute the fuction
print("f(" + str(pos) + ") = " + str(m))    #Print the result
