# Runtime Error
try:
    # Following line is taking user input
    # the future this may throw error.
    
    principle = int(input("Principle: "))

except ValueError:
    # when that error occur, what we must do
    # the code inside that except block  will get executed
    # only when an error occurs[]
    print("Principle amount must be an Integer")

except Exception as e:
    # Exception capture any error that can be happen
    print("Something went wrong:", e)

# The program does not get terminated abnormally

period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) / 100
print("Interest Amount: ",interest)

###############################################################################################
"""
Part Two
"""

def keyboardInput(datatype, caption, errorMessage):
    value = None
    inInvalid = True
    while(inInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
        return value

def calculateSimpleInterest():
    principle =keyboardInput(int, "Principle Amount:","Principle Amount must be integer")
    period = keyboardInput(float, "Period in years:", "Period must be float")
    rate = keyboardInput(float, "Rate in percentage: ", "Rate must be float")
    interest = (principle * period * rate) / 100
    print("Interest Amount: ", interest)
    print("Total amount to be paid:", principle + interest)

calculateSimpleInterest()
