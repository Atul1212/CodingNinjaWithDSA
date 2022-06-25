'''
Alpha Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26
Sample Input 1:
7
Sample Output 1:
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
Sample Input 2:
6
Sample Output 2:
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        charP = chr(ord('A') + i - 1)
        print(charP, end='')
        j = j + 1
        
    print()
    i = i + 1
