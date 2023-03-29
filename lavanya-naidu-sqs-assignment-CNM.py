import boto3
import sqs_module_assignment

prefix = 'lavanya-naidu-sqs-assignment-'
queue = sqs_module_assignment.create_queue(
        prefix + 'CNM',
        {
            'MaximumMessageSize': str(1024),
            'ReceiveMessageWaitTimeSeconds': str(20)
        }
    )
print(f"Created queue with URL: {queue.url}.")

sqs_module_assignment.send_message(queue.url)