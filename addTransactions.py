from Customer import Customer
#import json
from pymongo import MongoClient

client = MongoClient()
db = client.valuedCustomer
collection = db.transactions_first100000

#group lines that belong to the same id together
inputFile = open("/home/kuangyu/Desktop/transactions_first100000.csv", "r")
firstLine = inputFile.readline()
line = inputFile.readline()
currCustomerID = ""
currTransactions = []

while(line):
    #deal with first customer
    if currCustomerID == "":
        currTransactions.append(line)
        currCustomerID = line.split(",")[0]
    else:
        #line belong to the same customer
        if currCustomerID == line.split(",")[0]:
            currTransactions.append(line)
        else:
            #encounter new customer
            ## process the customer before first
            #print(currCustomerID + ":" + str(len(currTransactions)))
            lastCustomer = Customer(currTransactions)
            collection.insert(lastCustomer.toDict())
            #print(json.dumps(tmpDict))

            ## init new customer
            currCustomerID = ""
            currTransactions = []          
            currTransactions.append(line)

    line = inputFile.readline()

client.close()
