# Conversation Flow Analysis

## Project Overview

**Conversation Flow Analysis** is a Python-based tool for analyzing conversation flows in chatbots or virtual assistants. This project provides analysis capabilities for both **Google Dialogflow** and **Rasa NLU** models, identifying key insights such as detected intents, confidence levels, and entity extraction. It is useful for understanding the performance of conversation models, refining bot responses, and ensuring user intents are accurately captured.

## Features

- **Dialogflow Analysis**: Uses Google Dialogflow API to analyze user intents and responses.
- **Rasa Analysis**: Uses Rasa NLU models to analyze conversation transcripts, detect intents, and extract entities.
- **Session Analysis**: Evaluates user interactions to identify important insights, confidence scores, and more.

## Requirements

- Python 3.7 or higher
- Google Cloud Dialogflow SDK
- Rasa
- Dialogflow credentials (`key.json`)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Conversation-Flow-Analysis.git
cd Conversation-Flow-Analysis
```

### 2. Set up Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages

Install dependencies using pip:

```bash
pip install google-cloud-dialogflow rasa
```

### 4. Google Dialogflow Setup

Ensure you have your Dialogflow service account key (`key.json`) in the project root and update the `PROJECT_ID` in `dialogflow_analysis.py` with your Dialogflow project ID.

### 5. Rasa Model Setup

Place your Rasa NLU model in the `models/` directory and specify the path (`model_path`) in `rasa_analysis.py`. This model should be trained on intents relevant to your use case.

## Usage

Both scripts provide conversation flow analysis for different chatbot frameworks. You can run them separately depending on the chatbot model you're analyzing.

### 1. Dialogflow Analysis

To analyze conversation flow using Dialogflow, update `conversation_transcript` in `dialogflow_analysis.py` with your conversation data and run:

```bash
python dialogflow_analysis.py
```

Example output:
```plaintext
Query Text: Hi, I'm interested in your product.
Detected Intent: ProductInquiry (Confidence: 0.95)
Response: Hello! I'd be happy to help you with product information.

Query Text: Can you tell me more about the features?
Detected Intent: FeatureInfo (Confidence: 0.92)
Response: Sure, here are the main features...
```

### 2. Rasa Analysis

To analyze conversation flow using a Rasa NLU model, update `conversation_transcript` in `rasa_analysis.py` and set the correct path to your model in `model_path`. Then, run:

```bash
python rasa_analysis.py
```

Example output:
```plaintext
Query: Hi, I'm interested in your product.
Intent: greet (Confidence: 0.98)
Entities: []

Query: Can you tell me more about the features?
Intent: ask_features (Confidence: 0.91)
Entities: [{"entity": "feature", "value": "features"}]
```

## Code Overview

### dialogflow_analysis.py

- **`detect_intent_texts`**: Interacts with the Dialogflow API to analyze text input and return detected intents, confidence, and responses.
- **`analyze_conversation_flow`**: Processes a transcript to identify intents and responses for each user message.
- **`main`**: Sets a sample conversation transcript for analysis.

### rasa_analysis.py

- **`load_interpreter`**: Loads a pre-trained Rasa NLU model.
- **`analyze_conversation_flow`**: Parses each message in the transcript to detect intent and extract entities with Rasa NLU.
- **`main`**: Sets a sample conversation transcript for analysis.

## Contributing

Contributions are welcome! If you have improvements or new features to suggest, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Google Dialogflow](https://cloud.google.com/dialogflow) for providing powerful NLP capabilities.
- [Rasa](https://rasa.com/) for open-source conversational AI tools.
