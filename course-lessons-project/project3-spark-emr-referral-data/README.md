## Create an AWS EMR Cluster

1. Navigate to the EMR portion of the AWS console
2. Press "create cluster"
3. General configuration: a) Give the cluster a name, b) Configure logging with an S3 logging bucket, c) Set a launch mode (Cluster)
3. Software configuration: a) emr-5.16.0, b) Applications = Spark: Spark 2.3.1 ... No AWS Glue
4. Hardware configuration - a) m4.large b) 3 instances
5. Create a keypair, default permissions
6. Spin up cluster

## Login to the Cluster

1. Connect to the cluster via SSH with a command that looks like this: `ssh -i ~/Downloads/yoursshkey.pem hadoop@ec2-11-234-567-89.compute-1.amazonaws.com`
2. Respond yes to the prompt
3. After the machine has loaded you can now use Spark!

## Using Spark and PySpark

1. You can enter the PySpark shell with the `pyspark` command. This command starts up the PySpark shell and makes the Spark Context `sc` object available to you without having to do anything else.
2. If you want to be a rebel, you can enter the Scala shell with the `spark-shell` command.

## Processing Data with PySpark

1. Load `data-sample.txt` into S3 through the AWS console or the AWS CLI
2. Copy and paste the code from advertisers.py into the PySpark console
3. See the output result to S3

