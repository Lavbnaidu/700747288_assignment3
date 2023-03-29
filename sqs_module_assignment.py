import boto3
import logging
import json
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')

def create_queue(name, attributes=None):

    if not attributes:
        attributes = {}

    try:
        queue = sqs.create_queue(
            QueueName=name,
            Attributes=attributes
        )
        logger.info("Created queue '%s' with URL=%s", name, queue.url)
    except ClientError as error:
        logger.exception("Couldn't create queue named '%s'.", name)
        raise error
    else:
        return queue
    
def send_message(queue_url):
    sqs_client = boto3.client("sqs")
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=('This is my first queue message')
    )
    print(response)