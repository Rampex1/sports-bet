import json
import boto3
import logging
from datetime import datetime

# TODO:: Add the event bridge trigger to lambda when ready to test 


# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function triggered by EventBridge every 4 hours
    """
    try:
        logger.info("Lambda function started")
        logger.info(f"Event received: {json.dumps(event)}")
        
        # Your script logic goes here
        result = run_your_scripts()
        
        logger.info("Lambda function completed successfully")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Scripts executed successfully',
                'result': result
            })
        }
        
    except Exception as e:
        logger.error(f"Error executing scripts: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error executing scripts',
                'error': str(e)
            })
        }

def run_your_scripts():
    now = datetime.now()
    logger.info(f"The function is running at time: {now}")
    return str(now)

