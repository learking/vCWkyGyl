#group lines that belong to the same id together
inputFile = file("transaction_first100000.csv", "r")
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
            print(currCustomerID + ":" + str(length(currTransactions)))
            ## init new customer
            currCustomerID = ""
            currTransactions = []          
            currTransactions.append(line)

    line = inputFile.readline()  

#create JSON for each person


#insert JSON into mongoDB
