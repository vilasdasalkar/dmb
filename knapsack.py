def solve_knapsack():
     val=[50,100,150,200] #value array
     wt=[8,16,32,40] # Weight array
     W=64
     n=len(val) - 1
     def knapsack(W,n):
          if n<0 or W<=0:
              return 0
          if wt[n]>W:
              return knapsack(W, n-1)
          else:
              return max(val[n] + knapsack(W-wt[n],n-1),knapsack(W,n-1))


     print(knapsack(W,n))
 
if __name__=="__main__":
    solve_knapsack()
 

