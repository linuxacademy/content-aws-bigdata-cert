# IoT Data Project

## Creating Things, Certificates, and Policies

1. IoT --> Manage --> Show me later --> Register a thing --> Create a single thing
2. Create a thing called `store-thermometer-seattle1`
    Name it `store-thermometer-seattle1`

    Type --> Add a new type
        Name - `thermometer`
        Description - A thermometer
    
    Group 
        Name --> Seattle
        Description --> Things in Seattle
        Attributes --> (city | Seattle)

3. Create a certificate for the thing
    Certificate for the thing
        One-click certificate
        Download everything
        Download the first AWS certificate (not the symmatech one)

4. Create a policy for the thing and attach it to the certificate
    Policy for the thing
        Main IoT page > Secure > Policies > Create a policy
        Name - thermometer-policy
        Action - iot:*
        Resource ARN - *
            NOTE VERY PERMISSIVE DON'T DO IN PRODUCTION
        Check "Allow"
        Press create
    Attach Policy on the certificate we created
        Back to Secure > Certificates > attach policy

## Test subscribing and publishing to an IoT topic
    
1. Subscribe and publish to a topic
    IoT Core > Test
    Subscribe to a new topic `SeattleStoreTemp/1`
    Publish to it with the basic message

2. Setup a Python virtual environment for the IoT Script

```bash
python3 -m venv venv
source venb/bin/activate
pip install AWSIoTPythonSDK
```

From inside the Python interpreter Check that the OpenSSL version is 1.0.1 or greater
```python
import ssl
ssl.OPENSSL_VERSION
```

3. Publish to the same topic with the python script
    Edit the script (device_script.py)
        Change the BROKER_PATH
        Change the Root CA, Private Key and Certificate paths
    Use the script to publish to the topic and see it publish live in the browser

## Create a Rule to Process the Data
    Name - thermometer_rule
    Attributes - *
    OR Attributes - timestamp, temperature
    Topic Filter - SeattleStoreTemp/1
    Condition - wont use right now because we want all the data
    Add action
        Review integrations
        Send message to Amazon Kinesis Firehose
    Going to have to pause here and create a firehose 


## Creating a Firehose Delivery Stream for our IoT Rule
    Either Kinesis --> Firehose OR
    "Create new Resource" on the Configure Action stuff in IoT
    Create Stream
        Stream Name - weather-data-stream
        Direct Put
    Process records 
        Transform with Lambda - Off
        Transform Records for Glue - Off
    Destination 
        Amazon S3
        New S3 Bucket - la-big-data-seattle-weather-2018
    Settings 
        Buffer conditions 
            5MB
            300 seconds is fine
        Compression & Encryption options - off
        Error logging - Disabled
        IAM Role - Create a new one and take alook at it
    Review and create

## Finish up our IoT Rule
    Select the new stream name
    Separator - Newline
    Create a new role - iot-weather-data-role
    Select the role - iot-weather-data-role
    Add action
    Create the rule

## Testing our new IoT Rule
    Start the device_script.py again
    Check Firehose monitoring
    Check S3 for the actual data
    Note we could have delivered it directly with IoT
    Can modify it with Firehose