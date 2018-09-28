# Creating an Orders System

## Create the DynamoDB Table

1. Navigate to the DynamoDB portion of the AWS Console
2. Create a Table `PenguinOrders`
- Pick Partition Key (`order_id`) and optional sort key (`item_id`)
- Uncheck use defaults
- Mention LSI/GSI (You can look at the CDA and Labs for this)
- Set read/write capacity (Manually to 5 units each)
- Consider AutoScaling/Encryption but not in this case
- Create table

## Setting up the Script to Send in Data
1. Install dependencies and setup Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Make sure the table name is correct
3. Check that the credentials are correct with `aws dynamodb list-tables` to check that the table is there.
4. Run the script `python orders.py` OR `import orders` and `orders.write_orders()`
5. Pause it after a few entries and check that it works
6. Move on to creating the Lambda Function and ElasticSearch Cluster

## Creating the Lambda Function
1. Build the function package with
```bash
mkdir build && cd build
pip install -r ../dev-requirements.txt -t .
cp ../lambda_function.py .
zip -r ../package.zip ./* 
cd ..
rm -r build
mv ./package.zip ~/Desktop
```
2. Deploy the `package.zip` file in the AWS Console
3. Set a role for it that has permissions we need later
Role: 
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "es:ESHttpPost",
        "es:ESHttpPut",
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator",
        "dynamodb:ListStreams",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```
And trust relationship:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
4. Setup a trigger with DynamoDB streams using LATEST
5. Test it by briefly starting the script up again and seeing the function run and print to logs

## Creating the ElasticSearch Cluster
1. Create a cluster in ElasticSearch
    Name - `penguinorders`
    ES Version - 6.3
    Size - `t2.small.elasticsearch`
    Role - Open with IAM restrictions to the account and my IP?
2. Revisit the Role for the Lambda Function
3. Create an index in Kibana - `PUT orders` in the Dev Tools
4. Update the endpoint in the Lambda Function code
4. Test sending in data with the Lambda function by running the script again breifly

## Running and Testing Our Entire Order System
1. Run the script again and monitor the different areas you should see data moving through
2. DynamoDB - New Items
3. Lambda - Function Executions
4. ElasticSearch - New Indexed Documents
5. Leave the script running for 10ish min so that it can generate enough data for the data pipeline



