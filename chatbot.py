#6 Chatbot
!pip install nltk
import random
from difflib import get_close_matches

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "hii", "heyy", "yo", "sup"],
        "responses": ["Hello!", "Hi there!", "How can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "later"],
        "responses": ["Goodbye!", "Take care!"]
    },
    "ai": {
        "patterns": ["what is ai", "define ai", "artificial intelligence", "ai meaning"],
        "responses": ["Artificial Intelligence is the simulation of human intelligence in machines."]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "Happy to help!"]
    }
}

fallbacks = {
    "ai_deep": [
        "I'm still learning advanced AI topics.",
        "That's a deeper AI concept — I'm not trained on that yet."
    ],
    "unknown": [
        "I didn't quite get that. Can you rephrase?",
        "Not sure I understand. Ask something else?"
    ]
}

def clean_input(text):
    return text.lower().strip()

def match_pattern(user_input, patterns):
    match = get_close_matches(user_input, patterns, n=1, cutoff=0.6)
    return match[0] if match else None

def chatbot(user_input):
    user_input = clean_input(user_input)
    words = user_input.split()

    for intent in intents.values():
        for pattern in intent["patterns"]:
            if pattern in user_input or pattern in words:
                return random.choice(intent["responses"])
        match = match_pattern(user_input, intent["patterns"])
        if match:
            return random.choice(intent["responses"])

    if "ai" in user_input or "intelligence" in user_input:
        return random.choice(fallbacks["ai_deep"])

    return random.choice(fallbacks["unknown"])

print("Chatbot started (type 'bye' to exit)")

while True:
    msg = input("You: ")
    if msg.lower() == "bye":
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot(msg))
