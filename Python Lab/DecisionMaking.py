#Write a program to find whether the given number is positive, negative, or Zero
#Write a program to find whether our business is making profit, loss or breakeven

expenses = 1000
sales = 1100

#Objective 1: Say whether we are making loss or profit (single condition)
if (sales > expenses):
    #block of code
    print("You are making profit.")

print("Thank you")

#Objective 2: Say whether we are making loss or profit (2 condition)
if (sales > expenses):
    print("You are making Profit")
else:
    print("You are making Losses")

print("Thank you")

#Objective 3: Say whether we are making loss or profit (3 condition)
if (sales > expenses):
    print("You are making Profit")
else:
    if (sales == expenses):
        print("You are making Breakeven")
    else:
        print("You are making Losses")

print("Thank you")

if (sales > expenses):
    print("You are making Profit")
elif (sales == expenses):
    print("You are making Breakeven")
else:
    print("You are making Losses")

print("Thank You")

#find whether the given number is even or odd
#if the statement to be executed is not a block of code
# the statement can be write in same line

#find whether the given number is even
givennumber = 5
if(givennumber % 2 == 0): print("Even Number")

#find whether the given number is even or odd
print("Even number") if(givennumber % 2 == 0) else print("Odd number")

#find whether the given number is postive, negative or zero
print("Positive") if(givennumber > 0) else print("Negative") if(givennumber < 0) else print("Zero")