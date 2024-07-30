'''
Problem
Bob has a playlist of 
 songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob

Input Format 

The first line contains an integer 
, denoting the number of songs in Bob's playlist.

The following input contains 
 integers, 
 integer denoting the singer of the 
 song.

Output Format

Output a single integer, the number of favourite singers of Bob

Note: Use 64 bit data type

Constraints


Sample Input
5
1 1 2 2 4
Sample Output
2
Time Limit: 1
Memory Limit: 256
Source Limit:
Explanation
In this example
Songs of singer 1 and 2 appear 2 times(which is max) in this playlist 
Therefore the answer is 2
'''
n=int(input())
l=list(map(int,input().split()))
c={}
for i in range(n):
    if l[i] in c:
       c[l[i]]+=1  
    else:
        c[l[i]]=1
res=list(c.values())
count=res.count(max(res))
print(count)     # Writing output to STDOUT


