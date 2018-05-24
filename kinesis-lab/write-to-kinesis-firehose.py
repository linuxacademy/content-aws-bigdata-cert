import boto3
from faker import Faker
import random
import time
import json

DeliveryStreamName = 'linuxacademy-courses'

client = boto3.client('firehose')

fake = Faker()

courses = [
    "Linux+ LPIC Level 1 Exam 1",
    "Linux+ LPIC Level 1 Exam 2",
    "LPIC Level 2 Exam 201",
    "Mastering The Linux Command Line",
    "AWS Certified Developer - Associate Level ",
    "AWS Certified SysOps Administrator - Associate Level",
    "Introduction To Android Development",
    "OpenStack Essentials",
    "Learning Chef DevOps Deployment",
    "Docker Deep Dive ",
    "Learning Puppet DevOps Deployment (Puppet Professional Cert)",
    "AWS Certified DevOps Engineer - Professional Level",
    "Git and Git lab - Start to Finish",
    "Learning Vagrant ",
    "Linux Essentials Certification",
    "Linux Academy Red Hat Certified Systems Administrator Prep Course",
    "Nginx And The LEMP Stack",
    "Linux Security Essentials",
    "Jenkins and Build Automation",
    "Linux Foundation Certified Systems Administrator (Legacy)",
    "AWS Certified Solutions Architect - Associate Level",
    "AWS Certified Solutions Architect - Professional Level",
    "DevOps Essentials",
    "OpenStack MCA100 - Associates Certification",
    "Apache Tomcat 8 Application Server",
    "Deploying MariaDB Or MySQL On VPC EC2 From Scratch With Replication",
    "Linux Academy Red Hat Certified Engineer Prep Course",
    "SQL Primer",
    "Apache JBOSS Administration",
    "Learning Python 2.7 Development",
    "Machine Learning with Azure",
    "Amazon Machine Learning",
    "Azure IoT Essentials",
    "Nagios Certified Professional"
]




record = {}
while True:
    record['user'] = fake.name()
    record['course'] = random.choice(courses)
    record['video'] = random.randint(1, 10)
    record['timestamp'] = time.time()
    response = client.put_record(
        DeliveryStreamName=DeliveryStreamName,
        Record={
            'Data': json.dumps(record)
        }
    )
    print('PUTTING RECORD TO KINESIS: \n' + str(record))
