#!/usr/local/bin/python3

import boto3
import json
import sys

sqs = boto3.resource('sqs', region_name='eu-west-1')
queue = sqs.Queue('https://sqs.eu-west-1.amazonaws.com/332152328025/cafeteria.fifo')

def get_in_line(text):

    return queue.send_message(
        MessageBody=text,
        MessageGroupId='demo',
        MessageDeduplicationId='demo'
    )


if __name__ == '__main__':

    print(json.dumps(get_in_line(sys.argv[1])))
