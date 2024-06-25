name = "David"
batch = 101
fee = 1245.6578
#traditionally how we do this
inputstring = "Hello" + name + ", welcome to python class" + str(batch)
print(inputstring)

# special string called f string
inputstring = f"Hello {name}, welcome to python class {batch}"
print(inputstring)

# how much of space is required
inputstring = f"Hello {name:40s}, welcome to python class {batch}"
print(inputstring)

# align David to center
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

# align David to right
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

# provide padding characters
inputstring = f"Hello {name:*>40s}, welcome to python class {batch}"
print(inputstring)

# trucate to 3 character
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL for RM{fee:10.2f}"
print(inputstring)

# Binary
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM{fee:10.2f}"
print(inputstring)

#Oct
inputstring = f"Hello {name:.3}, welcome to python class {batch:o} in KL for RM{fee:10.2f}"
print(inputstring)

#Hex
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:10.2f}"
print(inputstring)