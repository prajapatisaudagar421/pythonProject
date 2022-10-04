def palindrome(num):
    reverse = 0
    n = num
    while(n != 0):
        remender = n%10;
        reverse = reverse*10+remender
        n = n//10
    if(num==reverse):
        print("yes")
    else:
        print("NO")
palindrome(121)