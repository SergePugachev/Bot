import random
import nltk

bot_config = {
    "hello": {
       "examples": ["hi", "hello", "sup", "whats up"],
       "responses": ["hi", "hello", "sup"]
    },
    "bye": {
        "examples": ["bye", "see ya", "goodbye"],
        "responses": ["bye", "see ya"]
    }
}


def filter(text):
    alphabet = 'qwertyuioplkjhgfdsazxcvbnm '
    result = [c for c in text if c in alphabet]
    return ''.join(result)


def match(text, example):
    text = filter(text.lower())
    example = example.lower()
    distance = nltk.edit_distance(text, example) / len(example)
    return  distance < 0.4


def get_answer(text):
    for intent in bot_config:
        for example in bot_config[intent]["examples"]:
            if match(text, example):
                return random.choice(bot_config[intent]["responses"])




