def fabonacci(num):
    n1 = 0
    n2 = 1
    next  = 0
    for i in range(1,num+1):
        print(n1,end="\t")
        next = n2+n1
        n1 = n2
        n2 = next
fabonacci(5)