import boto3

fraud_detector = boto3.client('frauddetector')

def detect_fraud(event_id, attributes):
    response = fraud_detector.get_event_prediction(
        detectorId='financial-fraud-detector',
        eventId=event_id,
        eventAttributes=attributes
    )
    print("Fraud Detection Result:", response)
