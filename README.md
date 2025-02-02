## ** Simple Lambda Login Alert **

Automated Alert to ensure no one is logging into my AWS Accounts Besides Me 

EventBridge Rule conects CloudTrail to trigger this lambda:

## Lambda Process
-- 
1. Recieved Alert From CloudTrail
2. Process Login Details
3. Publish to SNS Topic ARN

## Environment Variables 
- TOPIC_ARN - Arn of your SNS Topic, with specified emails/phone numbers subscribed to
