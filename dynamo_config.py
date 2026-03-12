"""
AWS Dynamodb table config.

Connect your CLI Writer to your AWS account to track:
1. Input data
2. AI output

 -- USAGE --
Type `aws configure` in the CLI to set AWS credentials.
"""
import os
from dotenv import load_dotenv
import boto3

# Load .env variables
load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name=os.getenv('AWS_REGION'))

table = dynamodb.create_table(
    TableName=os.getenv('TABLE_NAME'),
    KeySchema=[
        {
            'AttributeName': 'writeId', #PK
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'writeId',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.wait_until_exists()
# Confirm that the table is being created
print(f"Table status: {table.table_status}")
