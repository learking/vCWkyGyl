# parse one line of transaction record
class transactionRecord:
    def __init__(self, line):
        tmp = line.strip().split(",")
        self.customerID = tmp[0]
        self.chain = tmp[1]
        self.dept = tmp[2]
        self.category = tmp[3]
        self.company = tmp[4]
        self.brand = tmp[5]
        self.uniqueProductID = tmp[3]+","+tmp[4]+"," + tmp[5]
        self.dateInStrForm = tmp[6]
        self.productSize = float(tmp[7])
        self.productMeasure = tmp[8]
        self.purchaseQuantity = float(tmp[9])
        self.purchaseAmount = float(tmp[10])

# summarize all records for the same customer
# hold transactionRecord objects in self.transactions
# hold functions for feature construction
class oneCustomerRecord: 
    def __init__(self, line):
        self.transactions = []
        self.transactions.append(transactionRecord(line))
        self.customerID = self.transactions[0].customerID

    def addLine(self, line):
        self.transactions.append(transactionRecord(line))

    # feature 1: total purchase amount
    def getFeatureTotalPurchase(self):
        totalPurchaseAmount = 0
        for record in self.transactions:
            totalPurchaseAmount += record.purchaseAmount
        return totalPurchaseAmount

    # feature 3: total trip to store
    def getFeatureTotalTrips(self):
        datesVectors = []
        for record in self.transactions:
            datesVectors.append(record.datesVectors)
	return len(set(datesVectors))

    # function construct a list of features for a customer
    # return the list of features for the customer
    def getCustomerSummary(self):
        self.resultVector = []
        # call corresponding functions to get features here #
        # feature 1 - total amount of money spent by this customer
        self.resultVector.append(self.getFeatureTotalPurchase())
        # feature 2 - total number of transactions by this customer
        self.resultVector.append(len(self.transactions))
        # feature 3 - total number of trips to store measured by date
        self.resultVector.append(self.getFeatureTotalTrips())
        #
        return self.resultVector

inF = file("transaction.csv", "r")
outF = file("customerFeatures.csv", "w")
firstLine = inF.readline()
line = inF.readline()
lastCustomerID = ""
while(line):
    ### switch to next customer
    if(lastCustomerID == "" or customerObj.customerID != lastCustomerID):
        # record this customer
        if(lastCustomerID != ""):
            customerFeatureVector = customerObj.getCustomerSummary()
            outF.write(lastCustomerID + "," + ",".join(customerFeatureVector) + "\n")
        # construct new customer object
        customerObj = oneCustomerRecord(line) 
        lastCustomerID = customerObj.customerID
    
    ### adding record to current customer
    # since customerObj.customerID == lastCustomerID
    else:
        customerObj.addLine(line)
    
    ### new line, new transaction record
    line = inF.readline()

# read all transaction records complete, process for last customer
customerFeatureVector = customerObj.getCustomerSummary()
outF.write(lastCustomerID + "," + ",".join(customerFeatureVector) + "\n")
inF.close()
outF.close()
