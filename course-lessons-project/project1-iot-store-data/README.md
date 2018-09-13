# IoT Data Project

## Creating Things

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

    Certificate for the thing
        One-click certificate
        Download everything
        Download the first AWS certificate (not the symmatech one)

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

    




## Setup Python for IoT Script

```bash
python3 -m venv venv
source venb/bin/activate
pip install AWSIoTPythonSDK
```

Check - 
OpenSSL version 1.0.1+ (TLS version 1.2) compiled with the Python executable for X.509 certificate-based mutual authentication

```python
import ssl
ssl.OPENSSL_VERSION
```