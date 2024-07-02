# Runtime Error
try:
    # Following line is taking user input
    # the future this may throw error.
    
    principle = int(input("Principle: "))

except:
    #when that error occur
    print("Principle amount must be an Integer")