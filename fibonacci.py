def recur(n):
    first=0
    second=1
    print(first)
    print(second)
    
    while(n-2>0):
        third=first+second
        first=second
        second=third
        print(third)
        n-=1
recur(10)
    
