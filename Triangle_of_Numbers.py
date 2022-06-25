'''
Code : Triangle of Numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4



The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
'''

n = int(input())
k = 0
count = 0
count1 = 0
for i in range(1, n+1):
    for space in range(1,(n-i)+1):
        print(" ",end="")
        count+=1
        
    while k!=((2*i)-1):
        if count<=n-1:
            print(i+k, end="")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1),end="")
            
        k += 1
        
    count1 = count = k = 0
    print()
