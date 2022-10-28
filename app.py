import json
import requests

def handler(event, context):
    username = event['username']
    
    user_data = get_user_detail(username)
    return {
        'statusCode': 200,
        'body': json.dumps(user_data)
    }

def get_user_detail(username: str):
    user_data = requests.get('https://api.github.com/users/%s' % username).json()

    return user_data
