n=4
m= 5
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 or j==1 or i==n or j==m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
""""
output: 
* * * * * 
*       * 
*       * 
* * * * * 


IF WE WILL NOT USE ELSE CONDITION THE OUTPUT WILL COME LIKE THIS
* * * * * 
* * 
* * 
* * * * * 

"""