import re
import random
from datetime import datetime

def get_response(user_input):

    user_input = user_input.lower()

    greeting_responses = [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you.",
        "Hey! What can I do for you?",
        "Greetings!"
    ]

    patterns = {

        r".*\b(hi|hello|hey)\b.*":
            random.choice(greeting_responses),

        r".*\b(good morning)\b.*":
            "Good Morning! Hope you have a productive day.",

        r".*\b(good afternoon)\b.*":
            "Good Afternoon! How can I assist you?",

        r".*\b(good evening)\b.*":
            "Good Evening! Nice to see you.",

        r".*\b(your name|who are you)\b.*":
            "I'm CodSoft AI Assistant.",

        r".*\b(ai|artificial intelligence)\b.*":
            "Artificial Intelligence is the simulation of human intelligence by machines.",

        r".*\b(machine learning)\b.*":
            "Machine Learning enables computers to learn from data.",

        r".*\b(deep learning)\b.*":
            "Deep Learning uses neural networks with many layers.",

        r".*\b(python)\b.*":
            "Python is one of the most popular programming languages for AI.",

        r".*\b(java)\b.*":
            "Java is widely used for enterprise applications.",

        r".*\b(javascript)\b.*":
            "JavaScript is the language of the web.",

        r".*\b(weather)\b.*":
            "Sorry, I don't have access to live weather information.",

        r".*\b(time)\b.*":
            f"Current Time: {datetime.now().strftime('%H:%M:%S')}",

        r".*\b(date)\b.*":
            f"Today's Date: {datetime.now().strftime('%d-%m-%Y')}",

        r".*\b(joke)\b.*":
            "Why do programmers love dark mode? Because light attracts bugs!",

        r".*\b(thanks|thank you)\b.*":
            "You're welcome!",

        r".*\b(bye|goodbye)\b.*":
            "Goodbye! Have a great day."
    }

    for pattern, response in patterns.items():
        if re.match(pattern, user_input):
            return response

    return "Sorry, I couldn't understand that."