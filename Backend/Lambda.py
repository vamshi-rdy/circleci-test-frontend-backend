import os
import json
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    return {
        "statusCode": 202,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region
        })
    }
