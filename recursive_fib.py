def rec_fib(n):
    if n<=1:
        return n
    else:
        return rec_fib(n-1)+rec_fib(n-2)
        
if __name__=="__main__":
     n=10
     for i in range(n):
           print(rec_fib(i))



