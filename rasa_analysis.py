import json
import rasa
from rasa.nlu.model import Interpreter

def load_interpreter(model_path):
    """Load the Rasa NLU model."""
    return Interpreter.load(model_path)

def analyze_conversation_flow(transcript, interpreter):
    """Analyze the conversation transcript and identify key points."""
    for message in transcript:
        result = interpreter.parse(message)
        print(f"Query: {message}")
        print(f"Intent: {result['intent']['name']} (Confidence: {result['intent']['confidence']:.2f})")
        print(f"Entities: {result['entities']}\n")

def main():
    # Load the Rasa model
    model_path = "models"  # Specify your Rasa model path
    interpreter = load_interpreter(model_path)

    # Example conversation transcript (replace with your data)
    conversation_transcript = [
        "Hi, I'm interested in your product.",
        "Can you tell me more about the features?",
        "I'm not sure if this is right for me.",
        "What if I don't like it?",
        "Thanks for the information!"
    ]
    
    # Analyze conversation flow
    analyze_conversation_flow(conversation_transcript, interpreter)

if __name__ == "__main__":
    main()
