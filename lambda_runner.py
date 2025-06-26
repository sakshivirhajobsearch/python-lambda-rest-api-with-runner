# Runner to test Lambda locally
import json
from app import lambda_handler

if __name__ == "__main__":
    with open('event.json') as f:
        event = json.load(f)

    result = lambda_handler(event, None)

    print("Status Code:", result['statusCode'])
    print("Headers:", result['headers'])
    print("Body:", result['body'])
