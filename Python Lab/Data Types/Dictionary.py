# Python dictionary is also called JSON in other programming languages
# JavaScript Object Notation
# Dictionary is also using {}
# The data is ordered
# The data is indexed by key (not by number)
# Every single data is associated with a key
# For exp, firstnaem is a key and Peter is the data
# Key can't be duplicated, data can be duplicated
# it is modifiable

foreigner = {
    "firstname":"Peter",
    "lastname":"Parker",
    "passportnumber":"EA482736",
    "incometaxnumber":"MY34372",
    "pcbamount":826,
    "lastmonth": 5,
    "Lastyear":2024,
    "previousmonth":[(4,2024,891),(3,2024,895),(2,2024,893),(1,2024,892)],
    "addresses":{
        "office":{
            "street":"Jalan sultan ismail",
            "city":"Kuala Lumpur"
        },
        "home": {
            "street":"Jalan WM 3A/4",
            "city":"Behrang Stesen"
        }
    },
    "contact":"+60189580162"
}

print("First Name: ",foreigner["firstname"])
print("Last Name: ",foreigner["lastname"])
print("Passport Number: ",foreigner["passportnumber"])
print("Income Tax Number: ",foreigner["incometaxnumber"])
print("PCB Amount: ",foreigner["pcbamount"])
print("Last Month: ",foreigner["lastmonth"])
print("Last Year: ",foreigner["Lastyear"])
# print("Previous Month: ",foreigner["previousmonth"])
# print("Addresses: ",foreigner["addresses"])
# print("Contact: ",foreigner["contact"])

# item will hold a tuple (4, 2024, 891)
# however we know tuple is auto explode 
# as long as we have 3 variable we can explode and hold the 3 values
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year}  RM {amount}")

officeAddress = foreigner["addresses"]["office"]
print("\nOffice Addresses:")
print("Street:", officeAddress["street"])
print("City:", officeAddress["city"])
homeAddress = foreigner["addresses"]["home"]
print("\nHome Addresses:")
print("Street:", homeAddress["street"])
print("City:", homeAddress["city"])

# you can access the street directly as follow
foreigner["addresses"]["office"]["street"]
# print(test)

print("*"*100)
print(foreigner.keys())
for key in foreigner.keys():
    if(isinstance(foreigner[key],list)):
        for item in foreigner[key]:
            print(item)
    # elif (isinstance(foreigner[key], dict)):

    else:
        print(foreigner[key])

print("-"*100)

# when you use the method items you will get the key, value
for key,value in foreigner.items():
    print(key, value)

#how modify the dictionary
foreigner["car"] = {
        "brand":"Proton",
        "model":"SAGA",
        "carplate":"ALM345",
}
