# ./bin/pyspark

import csv
import json

# Get raw data
# Assumes headers are not present in files that are processed
rawAdPubData = sc.textFile("s3://temptemplatemptemp2018/data.csv")

cleanAdPubData = rawAdPubData.map(lambda line: list(csv.reader([line])))

# Sample the cleaned data
# cleanAdPubData.take(2)

# Remove the advertiser dimension and get a key value tuple in the form:
# ((publisher, datestring), sale_amount)
CleanPubData = cleanAdPubData.map(
    lambda row: (((row[0][1]), (row[0][2])), float(row[0][3]))
)

# Sampled the even cleaner data
# CleanPubData.take(2)


# Calculate publisher earnings based on 25% of goods sold
publisherDailyPayments = CleanPubData.aggregateByKey(
    0, 
    lambda a,b: a+b*.25,
    lambda c,d: c+d
)

def toJSONLine(data):
    return [data[0][0],data[0][1],str(round(data[1],2))]

# Sample what it looks like when we send the data back out
# publisherDailyPayments.map(toJSONLine).take(2)

# Flatten the data back into a format that can be sent to JSON
pubDailyPaymentsFlat = publisherDailyPayments.map(toJSONLine)

# Collect all the data into a single file (not usually what you'd do)
pubDailyPaymentsFlat.coalesce(1).toDF().write.save(
    "s3://temptemplatemptemp2018/adPubResultsjsontesttwo", 
    format="json"
)
