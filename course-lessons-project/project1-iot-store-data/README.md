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


