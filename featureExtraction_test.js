conn = new Mongo();
db = conn.getDB("valuedCustomer");

//for testing purpose:
//oneDoc = db.transactions_first100000.findOne();
//printjson( oneDoc );

//aggreg pipeline below is the work horse
db.transactions_first100000.aggregate( 
[
    { $unwind: "$transactions" },
    { $group :
      { _id : "$_id",
	totalPurchaseQuantity : { $sum : "$transactions.purchaseQuantity" } 
      } 
    },
    {
	$out : "features_test"
    }
]
)
