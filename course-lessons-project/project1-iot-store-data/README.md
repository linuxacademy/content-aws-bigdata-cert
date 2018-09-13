# IoT Data Project



## Migrating data automatically from S3 to Redshift with Glue

1. Navigate to Glue in the AWS Console
2. Create a crawler
3. Select the data store with the bucket and folder relevant to where the exisiting application exports it in S3
4. Create a Role for Glue
5. Setup a schedule for Glue to run with a given frequency:`0/5 * ? * * *`  EVERY FIVE MIN