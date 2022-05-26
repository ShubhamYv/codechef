n=4
for i in range(n+1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print("  ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print("  ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

"""
*             * 
* *         * * 
* * *     * * * 
* * * * * * * * 
* * * * * * * * 
* * *     * * * 
* *         * * 
*             * 
"""