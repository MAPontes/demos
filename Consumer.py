#!/usr/local/bin/python3

import boto3
import json
import sys

sqs = boto3.resource('sqs', region_name='eu-west-1')
queue = sqs.Queue('https://sqs.eu-west-1.amazonaws.com/332152328025/cafeteria.fifo')

def get_out():

    messages = queue.receive_messages()
    return messages[0].body

if __name__ == '__main__':

    print(get_out())
