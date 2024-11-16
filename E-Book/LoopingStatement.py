""" 1st Question - Count -
The Event organizers have announced to divide the children into two groups, to attend the competition in the two chosen galleries. By that note, all those children who have their registration code as an even number will be put in one gallery and those with odd number will be in another gallery.
Help the organizers to find count of number of even registration codes and odd registration codes from the total N
"""

entriesNum = int(input() )

entriesList = []
evenNum = 0
oddNum = 0

for i in range(entriesNum):
    entry =  int(input())
    entriesList.append(entry)
    if entry % 2 == 0:
        evenNum += 1
    else: 
        oddNum += 1

print(evenNum," ", oddNum)

""" 2nd - Hazecraft Client Series
The number of clients of the company from the start day of their journey till now is recorded sensibly and is seemed to have followed a specific series like 2,3,5,7,11,13,17,19, 23,…, etc

Write a program that takes an integer N as the input and will output the series till the Nth term.
"""

numN = int(input())

count = 0
givenNum = 2
while count < numN:
    isPrime = True
    for i in range(2, givenNum):
        if givenNum % i == 0:
            isPrime = False
            break
    if(isPrime == True):
            print(givenNum, end=" ")
            count += 1
    givenNum += 1



"""3rd - Series
The number of events that the company organizes every month is recorded sensibly and is seemed to have followed a specific series like: 30, 35, 38, 41, 54, 53 ...

Write a program which takes an integer N as the input and will output the series till the Nth term.
"""

num = int(input())

newList = []
firstNum = 30
secNum = 35
count = 0
count8 = 0
count6 = 0

while count < num:
    if(count % 2 == 0):
        firstNum += count8
        newList.append(firstNum)
        count8 += 8
    else:
        secNum += count6
        newList.append(secNum)
        count6 += 6
    count += 1

for a in newList:
    print(a, end=" ")


"""4th - Lucky Pairs
Richie and Riya are participating in a game called "Lucky pairs" at the Annual Game Fair in their Company. As per the rules of the contest, two members form a team and Richie initially has the number A and Riya has the number B.
There are a total of N turns in the game, and Richie and Riya alternatively take turns. In each turn the player whose turn it is, multiplies his or her number by 2. Richie has the first turn. Suppose after the entire N turns, Richie’s number has become C and Riya’s number has become D. The final score of the team will be the sum of the scores (C+D) of both the players after N turns.

Write a program to facilitate the quiz organizers to find the final scores of the teams.
"""

n = input()

sumScore = 0
numTurn = n.split(" ")

A, B, N = int(numTurn[0]), int(numTurn[1]), int(numTurn[2])

for i in range(N):
    if i % 2 == 0:
        A  *= 2
    else:
        B  *= 2
    N -= 1

sumScore = A + B

print(sumScore)

"""5th - Team Event
students who register for the event will be given a unique registration code N. The participants are teamed into 10 teams and the team to which a participant is assigned to depends on the absolute difference between the first and last digit in the registration code.

The event organizers wanted your help in writing an automated program that will ease their job of assigning teams to the participants. If the registration number given is less than 10, then the program should display "Invalid Input".
"""

givenNumber = input()

firstDigit = int(givenNumber[0])
lastDigit = int(givenNumber[-1])

if int(givenNumber) < 10:
    print("Invalid Input")
else:
    absDifference = abs(firstDigit -lastDigit )
    print(absDifference)


"""List Prime Number
o speed up his composition of generating unpredictable rhythms, A.R.Rahman wants the list of prime numbers available in a range of numbers.

Can you help him out?

Write a program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

Input Format:

Input consists of 2 integers which correspond to a and b. Assume that a is always less than or equal to b.

 

Output Format:

Refer sample output for details.

 

Sample Input 1:
2
15

Sample Output 1:
2 3 5 7 11 13
"""

#Code here

"""Bonus Question
Input Format:
First line of the input is an integer N.

Output Format:
Output a single line the series till Nth term, each separated by a comma.
Refer sample input and output for formatting specifications.

Sample Input 1:
5

Sample Output 1:
20 60 104 152 204
"""
N = int(input())

smallSeries = 40
Series = 20
count = 0
while count < N:
    print(Series, end = " ")
    Series += smallSeries
    smallSeries += 4
    count += 1

"""
Input Format:
First line of the input is an integer that refers to the number of lines in the pattern.

Sample Input 1:
4

Sample Output 1:
*******
b*iii*b
bb*i*bb
bbb*bbb
"""

"""
Input Format:
First 4 lines of the input correspond to the cost of a PINK, GREEN, RED, ORANGE ticket (in the exact order).
Last line of the input corresponds to the exact amount of money to be raised by selling tickets.

Output Format:
Output all combinations of tickets that produce exactly the desired amount to be raised. The combinations may appear in any order. Output the total number of combinations found. Output the smallest number of tickets to print to raise the desired amount so that printing cost is minimized.
Refer sample input and output for formatting specifications.

Sample Input 1:
1
2
3
4
3

Sample Output 1:
# of PINK is 0 # of GREEN is 0 # of RED is 1 # of ORANGE is 0
# of PINK is 1 # of GREEN is 1 # of RED is 0 # of ORANGE is 0
# of PINK is 3 # of GREEN is 0 # of RED is 0 # of ORANGE is 0
Total combinations is 3
Minimum number of tickets to print is 1
"""

"""
First line of the input is an integer contains two space-separated integers N (1 <= N <= 100) representing the number of ropes and an integer 'k'.
Second line of the input contains N integers separated by a single space, representing the ropes' lengths. Each rope length will not be less than 2 and will not be greater than 100.

Output Format:
Output a single line which contains a single integer representing the length of the final resulting rope.
Refer sample input and output for formatting specifications.

Sample Input 1:
3 1
3 4 6

Sample Output 1:
9

For example if a kid gets 3 ropes of lengths 3, 4 and 6 and k=1. He can connect 3 and 4 to get a rope of length 5, he then can connect the ropes of length 5 and 6 to get the final rope of length 9.

"""

"""Input Format:
The first line of the input contains one integer N (1 <= N <= 100) representing the number of problem sets and the number of trainees.
The second line of the input contains N non-negative integers separated by a single space, representing the number of problems in each problem set. Each problem set will contain at most 100 problems.

Output Format:
Output a single line that will contain the minimum number of problems to be deleted, followed by space than the minimum number of problems to be moved.
Refer to sample input and output for formatting specifications.

Sample Input 1:
3
3 3 3

Sample Output 1:
0 0
"""


"""
13 is divisible by 1
14 is divisible by 2
15 is divisible by 3
16 is divisible by 4
17 is NOT divisible by 5
So streak(13)=4.
Similarly:
120 is divisible by 1
121 is NOT divisible by 2
So streak(120)=1.

Now, define P(k, N) which will give the number of integers n, 1<n<=N, for which streak(n) = k. Write a program to get the input as 'k' and 'N' and,
find the count of integers until N which has the streak value as 'k'.

Input Format:

The first line of the input is an integer ‘k’ which is the streak value of an integer n.
The second line of the input is an integer ‘N’ which is the upper limit of numbers until which P(k, N) is calculated.

Sample Input 1:

3
14

Sample Output 1:

1
"""