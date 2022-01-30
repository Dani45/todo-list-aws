import os
import json
import decimalencoder
import todoList
import boto3
dynamodb = boto3.resource('dynamodb')
traductor = boto3.client('translate',region_name='us-east-1')

def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = todoList.get_item(event['pathParameters']['id'])

    source_language = 'auto' # Dejamos que Amazon Comprehend detecte el lenguaje origen
    target_language = event['pathParameters']['language']

    result_trad = traductor.translate_text(Text=result['Item'], SourceLanguageCode=source_language, TargetLanguageCode=target_language)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result_trad.get('TranslatedText'),
                           cls=decimalencoder.DecimalEncoder)
    }

    return response