givenNumber = 9
divisors = range(2, givenNumber)

if (len([mynumber for mynumber in divisors if(givenNumber % mynumber == 0)])==0):
    print("Prime Number")
else:
    print("Not Prime Number")

