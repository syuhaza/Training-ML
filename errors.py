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
