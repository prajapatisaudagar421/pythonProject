def armstrong(num):
    n = num
    n1 = num
    sum =0
    count =0
    while(n1 != 0):
        count = count+1
        n1 = n1//10
    while n != 0:
        remender = n%10
        sum = sum + pow(remender,count)
        n = n//10
    if num == sum:
        print("yes")
    else:
        print("no")
armstrong(153)
