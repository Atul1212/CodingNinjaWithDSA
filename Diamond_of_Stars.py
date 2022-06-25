'''
Diamond of Stars
Send Feedback
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *

'''

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
first=n//2+1
sec=n//2
#first loop
for i in range(1,first+1):
    print(" "*(first-i),end="")
    print((2*i-1)*"*",end="")
    print()
#Second Loop
for p in range(1,sec+1):
    print(" "*p,end="")
    print((2*(sec-p+1)-1)*"*",end="")
    print()
