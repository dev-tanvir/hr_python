"""
python > bulit-ins > athlete sort

You are given a spreadsheet that contains a list of N  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the k-th attribute and print the final resulting table. Follow the example given below for better understanding.

Note that  is indexed from 0 to M-1, where  is the M number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space. 
The next N lines each contain M elements. 
The last line contains k.

Constraints

 0<= k < M
 
Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since k is zero-indexed.

"""

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
def sortKey(elem):
  return elem[k]
  
arr.sort(key = sortKey)

for i in arr:
    print(*i)                  #unpacking before printing
