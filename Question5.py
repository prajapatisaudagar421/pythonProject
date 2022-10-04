def factorial(num):
    fact = 1
    if num<0:
        print("factorial of a negative number doesn't exist")
    else:
        for i in range(1,num+1):
            fact = fact*i
    print(fact)



factorial(5)

def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
print(fact(5))