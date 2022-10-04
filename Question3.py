def sumOfDigits(num):
    sum = 0
    while num != 0:
        remender = num%10
        sum = sum + remender
        num = num//10
    print(sum)
sumOfDigits(1357)