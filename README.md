# Combating Spam Calls, Deepfake Fraud, and VKYC Exploitation in Financial Services

## Overview
This project provides an AI-powered solution leveraging AWS services to detect and prevent:
1. **Spam Calls**: Identifying phishing and scam calls using NLP.
2. **Deepfake Fraud in VKYC**: Using computer vision and audio analysis to detect deepfake attempts.
3. **Financial Fraud**: Monitoring transaction anomalies to detect fraudulent activities.

## Features
- **Spam Call Detection**: Analyze call transcripts for suspicious patterns and keywords.
- **VKYC Deepfake Detection**: Real-time analysis of manipulated video/audio inputs.
- **Financial Fraud Detection**: Detect unauthorized transactions using machine learning models.

## Architecture
The solution integrates multiple AWS services, including Amazon Transcribe, Comprehend, Rekognition, Fraud Detector, and Lambda, for real-time analysis.

## Repository Structure
- `architecture/`: Contains the architecture diagram.
- `scripts/`: Python scripts for detection modules.
- `aws_cloudformation/`: Infrastructure setup template.
- `docs/`: Presentation slides.
- `requirements.txt`: Dependencies for running the solution.

## How to Run
1. Deploy the infrastructure using the CloudFormation template.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the detection scripts with sample data for each module.

## AWS Services Used
- Amazon Rekognition
- Amazon Transcribe
- Amazon Comprehend
- Amazon Fraud Detector
- AWS Lambda
