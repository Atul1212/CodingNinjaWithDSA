'''
Number Star pattern 1
Send Feedback
Print the following pattern for given number of rows.
Input format :
Integer N (Total number of rows)
Output Format :
Pattern in N lines
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321
'''
lines= int(input()) 
i=1  
while(i<=lines):# this loop is used to print lines  
    j=lines  
    while (j>=1):# this loop is used to print numbers in a line  
        if j!=i:  
            print(j, end='', flush=True)  
        else:  
            print('*', end='', flush=True)  
        j=j-1  
    print("")  
    i=i+1;  
    
    '''
    Zeros and Stars Pattern
Send Feedback
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
    '''
n = int(input())
rows = 2*n + 1
i = 1

while i <= n:
    j = 1
    while j <= rows:
        if(j == i or j == (rows // 2 + 1) or j == rows - i +1):
            print('*',end = '')
            
        else:
            print('0',end = '')

        j = j + 1
        
    print()
    i = i + 1
      
'''
Check Armstrong
Send Feedback
Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
Input Format :
Integer n
Output Format :
true or false
Sample Input 1 :
1
Sample Output 1 :
true
Sample Input 2 :
103
Sample Output 2 :
false
'''
def checkArmstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
        
    if num == sum:
        return True
    return False

num = int(input())
isArmstrong = checkArmstrong(num)
if(isArmstrong):
    print('true')
else:
    print('false')

