#command line is also called command line arguments
#arguments are separated by space
#arguments are separated by comma
#sys.argv give us a list, which contain all the command line arguments
import sys

cmdarguments = sys.argv #we are using . (dot) operator
print(cmdarguments)

#find the total of all arguments
#if we know the total number of arguments 
#total = int(cmdarguments[1] + cmdarguments[1])

total = 0
for number in cmdarguments[1:]:
    total = total + int(number)
print(total)