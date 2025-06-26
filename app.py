# Main Lambda function (handler)
import json

def lambda_handler(event, context):
    path = event.get("path", "")
    http_method = event.get("httpMethod", "")
    query_params = event.get("queryStringParameters") or {}

    # Handle favicon.ico to avoid 403/404 browser requests
    if path == "/favicon.ico":
        return {
            "statusCode": 204,
            "headers": {
                "Content-Type": "image/x-icon",
                "Access-Control-Allow-Origin": "*"
            },
            "body": ""
        }

    # Handle GET /hello
    if path == "/hello" and http_method == "GET":
        name = query_params.get("name", "World")
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": f"Hello, {name}!"})
        }

    # Handle all other paths
    return {
        "statusCode": 404,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"error": "Not Found"})
    }
