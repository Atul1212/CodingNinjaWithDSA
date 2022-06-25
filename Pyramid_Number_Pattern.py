'''
Pyramid Number Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print('')
