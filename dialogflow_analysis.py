import os
import json
from google.cloud import dialogflow_v2 as dialogflow

# Set up Dialogflow client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
PROJECT_ID = "a1b2c3d4e5"

def detect_intent_texts(project_id, texts, language_code):
    """Detect the intent of the user's text."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, "unique-session-id")

    responses = []
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        responses.append(response)
    
    return responses


def analyze_conversation_flow(transcript):
    """Analyze the conversation transcript and identify key points."""
    language_code = 'en'
    responses = detect_intent_texts(PROJECT_ID, transcript, language_code)

    for response in responses:
        print(f"Query Text: {response.query_text}")
        print(f"Detected Intent: {response.intent.display_name} (Confidence: {response.intent_detection_confidence})")
        print(f"Response: {response.fulfillment_text}\n")


def main():
    # Example conversation transcript (replace with your data)
    conversation_transcript = [
        "Hi, I'm interested in your product.",
        "Can you tell me more about the features?",
        "I'm not sure if this is right for me.",
        "What if I don't like it?",
        "Thanks for the information!"
    ]
    
    # Analyze conversation flow
    analyze_conversation_flow(conversation_transcript)


if __name__ == "__main__":
    main()
