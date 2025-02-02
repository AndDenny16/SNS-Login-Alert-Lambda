## ** Simple Lambda Login Alert **

Automated Alert to ensure no one is logging into my AWS Accounts Besides Me 

## EventBridge Rule 

- JSON Rule
- Connect CloudTrail Console Login API Call to Lambda
- Edit the ARNs to your desired accounts, you want to be notified about

## Lambda Process

1. Recieved Alert From CloudTrail
2. Process Login Details
3. Publish to SNS Topic ARN

## Lambda Environment Variables 
- TOPIC_ARN - Arn of your SNS Topic, with specified emails/phone numbers subscribed to
