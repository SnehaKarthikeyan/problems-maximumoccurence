# problems-maximumoccurence

Question:

Given a number N and array of N integers, find the number which occurs the maximum number of times.
Input Size : |N| <= 1000000


Input Description: 

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements.

Output Description: 

Print the integer value which occurs the maximum number of times.

Hints:

Create a Map of characters to their frequency. Traverse through the map and find which element has the highest frequency.

Sample Input:

11\n
51 2 6 2 2 6 2 3 6 6 2

Sample Output:

2

Explanation:

As in the test case, 2 occurs the maximum number of times in the given array, the output is 2.

Testcase 1:

Input:

23\n
25 73 51 34 56 78 51 22 13 56 77 51 34 97 51 22 45 70 55 33 51 36 23

Output:

51

Testcase 2:

Input:

20\n
1125 1173 1251 1334 2112 5126 3378 5651 6722 1903  4456 7457 2112 5144 3443 9722 5111 2112 4445 1227

Output:
 
2112

Testcase 3:

Input:

21\n
11 25 45 55 67 11 73 67 34 56 78 67 22 43 54 66 87 67 23 45 68

Output:

67

Testcase 4:

Input:

24\n
4 51 6 12 34 3 43 2  5 34 78 66 45 78 93 22 6 45 23 56 79 99 54 2

Output:
 
6

Testcase 5:

Input:

22\n
4 51 6 12 34 3 33 56 78 3 12 45 98 3 22 56 3 78 90 43 11 25 

Output:

3
