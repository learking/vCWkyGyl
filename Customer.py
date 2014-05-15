class Customer:
    def __init__(self, lines):
        self._id = lines[0].split(",")[0]
        self.transactions = self.getTransactions(lines)

    def getTransactions(self, lines):
        transactions = []
        for line in lines:
            transactions.append(self.transaction2dict(line))
        return transactions

    def transaction2dict(self, line):
        tmp = line.strip().split(",")

        resultDict = {
            "chain" : tmp[1] ,
            "dept" : tmp[2] ,
            "category" : tmp[3] ,
            "company" : tmp[4] ,
            "brand" : tmp[5] ,
            #"uniqueProductID" : tmp[3]+","+tmp[4]+"," + tmp[5] ,
            "date" : tmp[6] ,
            "productSize" : float(tmp[7]) ,
            "productMeasure" : tmp[8] ,
            "purchaseQuantity" : float(tmp[9]) ,
            "purchaseAmount" : float(tmp[10]) 
            }
        return resultDict

    def toDict(self):
        return(
            {
                "_id": self._id,
                "transactions": self.transactions
                }
            )
