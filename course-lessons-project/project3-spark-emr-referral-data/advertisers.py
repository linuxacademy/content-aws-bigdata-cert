# ./bin/pyspark

def cleaner(s):
    return str(s).replace('"','').strip(' ')

def to_csv(d):
    return str(d[0][0])+','+str(d[0][1])+','+str(d[1])

def toCSVLine(data):
  # data = t[0]
  return data[0][0] + ',' + data[0][1] + ',' + str(data[1])

# Get raw data from the data
# Assumes headers are not present in files that are processed
rawAdPubData = sc.textFile("s3://emr-test-la-2018/data-sample.txt")
# rawAdPubData = sc.textFile('./databig.csv')
# rawAdPubData = sc.textFile('./final.csv')

# Sample the data
# rawAdPubData.take(2)

# Split lines up
cleanAdPubData = rawAdPubData.map(lambda line: line.split(","))

# Sample the cleaned data
# cleanAdPubData.take(2)

# Remove the advertiser dimension and get a key value tuple in the form:
# ((publisher, datestring), sale_amount)
CleanPubData = cleanAdPubData.map(
    lambda row: ((cleaner(row[1]), cleaner(row[2])), float(row[3]))
)

# Sampled the even cleaner data
# CleanPubData.take(2)

# Calculate publisher earnings based on 25% of goods sold
publisherDailyPayments = CleanPubData.aggregateByKey(
    0, 
    lambda a,b: a+b*.25,
    lambda c,d: c+d
)

# Sample what it looks like when we retransform it to a csv
# publisherDailyPayments.map(toCSVLine).take(2)

# Send over to s3
publisherDailyPayments.map(toCSVLine).saveAsTextFile("s3://emr-test-la-2018/output-sample-csv-three")

