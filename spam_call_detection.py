import boto3
import time

# Initialize AWS clients
transcribe = boto3.client('transcribe')
comprehend = boto3.client('comprehend')
sns = boto3.client('sns')

def detect_spam_call(audio_url, topic_arn):
    # Generate a unique job name
    job_name = f"SpamCallDetectionJob-{int(time.time())}"
    
    # Start the transcription job
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': audio_url},
        MediaFormat='mp3',
        LanguageCode='en-US',
        NotificationChannel={
            'RoleArn': 'arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_ROLE',
            'SNSTopicArn': topic_arn
        }
    )
    
    print("Transcription job started. Awaiting results...")

def poll_transcription_status(job_name):
    # Poll the transcription job status
    while True:
        response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        status = response['TranscriptionJob']['TranscriptionJobStatus']
        
        if status == 'COMPLETED':
            transcript_url = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
            print(f"Transcription completed. Transcript URL: {transcript_url}")
            return transcript_url
        elif status == 'FAILED':
            print("Transcription failed.")
            return None
        else:
            print("Waiting for completion...")
            time.sleep(10)

def analyze_transcript_and_classify_spam(transcript_url):
    # Fetch the transcript content
    transcript_response = boto3.client('s3').get_object(Bucket='YOUR_BUCKET', Key=transcript_url)
    transcript_text = transcript_response['Body'].read().decode('utf-8')

    # Use AWS Comprehend to detect sentiment and entities
    sentiment = comprehend.detect_sentiment(Text=transcript_text, LanguageCode='en')
    entities = comprehend.detect_entities(Text=transcript_text, LanguageCode='en')
    
    print(f"Sentiment Analysis: {sentiment['Sentiment']}")
    print(f"Entities Detected: {entities['Entities']}")

    # Check for spammy words or phrases in the entities or sentiment
    spam_keywords = ['free', 'winner', 'prize', 'claim', 'unlimited', 'money']
    for entity in entities['Entities']:
        if any(keyword in entity['Text'].lower() for keyword in spam_keywords):
            print("Spam detected based on entity detection.")
            return True

    if sentiment['Sentiment'] == 'NEGATIVE' and 'questionable' in transcript_text.lower():
        print("Spam detected based on negative sentiment and content.")
        return True

    return False

def main(audio_url, sns_topic_arn):
    detect_spam_call(audio_url, sns_topic_arn)
    job_name = "SpamCallDetectionJob"  # Ensure this is dynamic based on real use-case
    transcript_url = poll_transcription_status(job_name)
    
    if transcript_url:
        is_spam = analyze_transcript_and_classify_spam(transcript_url)
        if is_spam:
            print("This call is classified as spam.")
        else:
            print("This call is not spam.")

# Example usage
audio_url = "https://path-to-audio-file"
sns_topic_arn = "arn:aws:sns:region:account-id:topic-name"
main(audio_url, sns_topic_arn)
