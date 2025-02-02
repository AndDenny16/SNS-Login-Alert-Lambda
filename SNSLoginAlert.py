import json
import boto3
import os 

def lambda_handler(event, context):
    print("Received event")
    sns_client = boto3.client("sns")

    detail = event.get("detail", {})
    user_identity = detail.get("userIdentity", {})
    event_source = detail.get("eventSource", "Unknown")
    event_time = event.get("time", "Unknown Time")
    
    message = message = f"""
            AWS Login Alert:
            Event Source: {event_source}
            User Type: {user_identity.get('type', 'Unknown')}
            User Name: {user_identity.get('userName', 'Unknown')}
            Event Time: {event_time}
            """

    TOPIC_ARN = os.getenv("TOPIC_ARN")
    sns_response = sns_client.publish(
        TopicArn=TOPIC_ARN,  
        Message=message,
        Subject="AWS Login Alert"
    )
    print("SNS publish response:", sns_response)
    
    return {
        'statusCode': 200,
        "body": "Notification sent successfully."
    }
