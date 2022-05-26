n= 5
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

"""OUTPUT:
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
        """


for i in range(n+1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


"""OUTPUT:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""