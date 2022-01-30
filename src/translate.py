# from pprint import pprint
import warnings
import unittest
import boto3
from moto import mock_dynamodb2
import sys
import os
import json

import todoList

def translate(event, context):
     # fetch todo from the database
    result = todoList.translate_todo(event['pathParameters']['id'],event['pathParameters']['language'])

    response = {
        "statusCode": result['status_code'],
        "body": result['message'] }

    return response