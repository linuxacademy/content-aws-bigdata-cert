# Creating a Redshift Cluster

1. Navigate to Redshift in the AWS console
2. Quick Launch a 1-node cluster
3. Install Postico
4. Install the [JDBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver)
5. Copy Redshift JDBC url. e.g. `redshift-cluster-1.ccmcujfidyml.us-east-1.redshift.amazonaws.com` port `5439` and `dev` database

# Loading Data into Redshift

## Loading data from EMR via S3

1. Process data with EMR
2. Export data from EMR to S3
3. Create an IAM role for Redshift to use to copy the data from S3 to redshift
4. Create a table to store the data 
```sql
create table pubearnings(
    earnings_id bigint identity(1, 1),
    publisher varchar(100),
    pubdate date,
    earnings REAL,
primary key(earnings_id));
```

5. Load data from S3 to new Redshift table
```sql
copy pubearnings
from 's3://emr-test-la-2018/output-sample-csv-three'
IAM_ROLE 'arn:aws:iam::218856049422:role/redshift-ro-s3'
DATEFORMAT AS 'MM/DD/YYYY'
FORMAT AS CSV;
```
