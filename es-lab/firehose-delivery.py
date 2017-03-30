import datetime
import boto3
import random
import time
import json

DeliveryStreamName = 'linuxacademy-courses'

client = boto3.client('firehose')



courses = [
    "Linux+ LPIC Level 1 Exam 1",
    "Linux+ LPIC Level 1 Exam 2",
    "LPIC Level 2 Exam 201",
    "Mastering The Linux Command Line",
    "AWS Certified Developer - A ",
    "AWS Certified SysOps Administrator - A",
    "Introduction To Android Development",
    "OpenStack Essentials",
    "Learning Chef DevOps Deployment",
    "Docker Deep Dive ",
    "AWS Certified DevOps Engineer - Pro",
    "Git and Git lab - Start to Finish",
    "Learning Vagrant ",
    "Linux Essentials Certification",
    "Nginx And The LEMP Stack",
    "Linux Security Essentials",
    "Jenkins and Build Automation",
    "AWS Certified Solutions Architect - A",
    "AWS Certified Solutions Architect - Pro",
    "DevOps Essentials",
    "OpenStack MCA100 - Associates Certification",
    "Apache Tomcat 8 Application Server",
    "SQL Primer",
    "Apache JBOSS Administration",
    "Learning Python 2.7 Development",
    "Machine Learning with Azure",
    "Amazon Machine Learning",
    "Azure IoT Essentials",
    "Nagios Certified Professional"
]




dt = datetime.datetime(2016, 12, 01)
end = datetime.datetime(2017, 12, 30, 23, 59, 59)
step = datetime.timedelta(seconds=60)

record = {}

while dt < end:
    dt += step
    record['course'] = random.choice(courses)
    record['active_users'] = random.randint(1, 100)
    record['date_time'] = dt.strftime('%Y-%m-%d %H:%M:%S')
    response = client.put_record(
        DeliveryStreamName=DeliveryStreamName,
        Record={
            'Data': json.dumps(record)
        }
    )
