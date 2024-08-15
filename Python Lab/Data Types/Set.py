# Set uses {}
# Set is modifiable (add, edit, delete)
# Set is unordered (the items retain its position)
# doesnt indexed (do not have 0,1,2,3,4,5,....)
# doesn't allow duplicates
# a given element cant appear in a set more than once

# in python this is the first time we are using {}
x = {10,20,30,10,40,50,20,60,70}
print(x)
# what do you observe
# 1) numbers are not in the same order as it was created
# 2) duplicate numbers are missing

# since set is not indexed you cannot retrieve the values using [] syntax
# to retrieve the items inside the set
# only way is use for loop
for i in x:
    print(i)

fruits = {"apple","orange","mango"}
fruits.add("durian") # add at a random place
print(fruits)

# to delete an item in the set
fruits.remove("orange")
print(fruits)

# pop => randomly removes an item in the set
fruits.pop()
print(fruits)

# if you want to update an item
# 1) remove the item
# 2) add the new item
print("="*100)
#set() tuple() dictionary() range are class
fruits = ["apple","orange","apple","mango","banana","apple"]
uniquesFruits = set(fruits) #remove duplicates
print(uniquesFruits)

# list(range(0,10)) take iterator object
# tuple(range(0,10))
# list(enumerate(["apple","orange"]))
# iterator object / that contains a countable number of values. 
# Lists, tuples, dictionaries, and sets are all iterable objects (Iterators)
# Function always return the number/others
# Class will always return the object / instance of a class

overseafruits = {"apple","orange","mango","banana","grapes"}
localFruits = {"banana", "durian","rambutan","cempedak","mangosteen"}
print(overseafruits.union(localFruits))
print(overseafruits.intersection(localFruits))
print(overseafruits.difference(localFruits))
print(localFruits.difference(overseafruits))

favoritefruits = {"mangosteen","rambutan","cempedak"}
print(favoritefruits.issubset(localFruits))
print(localFruits.issuperset(favoritefruits))
print(favoritefruits.isdisjoint(overseafruits))
print("="*100)

# Split Character
emailcontent = """ What phishing is. Phishing is an attempt to steal personal information or break in 
to online accounts using deceptive emails, messages, ads, or sites that look similar to sites you already use. 
For example, a phishing email might look like it's from your bank and request private information about your bank account.
Scammers use email or text messages to try to steal your passwords, account numbers, or Social Security numbers. 
If they get that information, they could get access to your email, bank, or other accounts. 
Or they could sell your information to other scammers. Scammers launch thousands of phishing attacks like these every day — 
and they’re often successful.
"""

words = emailcontent.split()
print(len(words))

uniqueswords = set(words)
print(len(uniqueswords))
print(uniqueswords)

cleanwords = []
for word in words:
    # word is instance of string class on word is a string object
    # remove is a metjod inside the word object
    # remove takes 2 arguments first argument is used to find
    # second argument is used to replace
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.lower()
    cleanwords.append(word)

uniqueswords = set(cleanwords)
print(len(uniqueswords))

print(uniqueswords)

commonwords = {"is","or","of","so","by","how","when","it","on","the","into",
               "a","to","is","are","what","be","i","you","more","and","can","an","it's"}

uniqueswords = uniqueswords.difference(commonwords)
print(uniqueswords)
print(len(uniqueswords))

spamwords = {"tricked","trick","pishing","security","criminals"}
numSpamwords = uniqueswords.intersection(spamwords) # To see how many spams words do we have
print(len(numSpamwords))
# Here we try to demonstrate the features of set data structure

# define the set{'a','b','c'}
s = set(['a','b','c'])
s = set({'a','b','c'}) # at mcq iExplore set{('a','b','c')}
s = set('abc')